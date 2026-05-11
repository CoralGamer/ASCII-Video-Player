"""
ASCII Art Video Player - Versión 5 (Ultimate / CLI)
====================================================
Versión completa con argparse CLI. Basado en el trabajo de @stepanussaruran.

Características:
  - argparse: todas las opciones vía línea de comandos
  - flag --color / --no-color
  - --width, --skip (salta cada N cuadros para mayor velocidad)
  - --loop para repetir el video
  - --info para mostrar solo la información del video sin reproducir
  - Hilo de decodificación en segundo plano (siempre activo)
  - Cierre seguro (Graceful shutdown)

Créditos Originales: stepanussaruran
Traducción y Mejoras: Nicolas Romero (coralgamer)
Licencia: MIT (Open Source)
=====================================================
ACTUALIZADO POR: CORALGAMER
AGREGADO BY: CORALGAMER
CHANGELOG:
- Traducción completa al español (Interfaz, Comentarios y Ayuda).
- Soporte para ajuste automático al tamaño de la terminal (Ancho y Alto).
- Implementación de relación de aspecto dinámica para evitar estiramientos.
- Barra de estado fija en la última línea de la terminal para evitar parpadeos.
- Mejoras en el modo interactivo (preguntas para Color, Ajuste, Bucle y Salto).
- Optimización de la lógica de renderizado dinámico.
=====================================================
""" 

import argparse
import cv2
import os
import sys
import time
import threading
import numpy as np
from queue import Queue, Empty

# ── Conjunto de 92 caracteres ──────────────────────────────────────────────────
ASCII_CHARS = (
    " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu"
    "[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
)
_CHARS_ARRAY = np.array(list(ASCII_CHARS))

# ── Códigos de Escape ANSI ───────────────────────────────────────────────────
CURSOR_HOME  = "\033[H"
CLEAR_SCREEN = "\033[2J"
HIDE_CURSOR  = "\033[?25l"
SHOW_CURSOR  = "\033[?25h"
RESET_COLOR  = "\033[0m"

# ── Colores de texto para la interfaz ─────────────────────────────────────────
C_CYAN   = "\033[96m"
C_GREEN  = "\033[92m"
C_YELLOW = "\033[93m"
C_RED    = "\033[91m"
C_GRAY   = "\033[90m"
C_BOLD   = "\033[1m"


# ── Utilidades ───────────────────────────────────────────────────────────────

def enable_ansi_windows() -> None:
    """Activa los códigos de escape ANSI en Windows."""
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass


def get_video_info(cap: cv2.VideoCapture) -> dict:
    """Obtiene los metadatos del video."""
    return {
        "fps"          : cap.get(cv2.CAP_PROP_FPS),
        "total_frames" : int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        "width_px"     : int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height_px"    : int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "duration_s"   : cap.get(cv2.CAP_PROP_FRAME_COUNT) / max(cap.get(cv2.CAP_PROP_FPS), 1),
    }


# ── Utilidades de Interfaz Premium ──────────────────────────────────────────

def clear_console():
    """Limpia la terminal completamente."""
    sys.stdout.write(CLEAR_SCREEN + CURSOR_HOME)
    sys.stdout.flush()

def draw_box_title(title: str, subtitle: str = "", show_giant_cat: bool = True):
    """Dibuja un encabezado estilizado que se ajusta a terminales estrechas."""
    term_cols = os.get_terminal_size().columns
    # Evitar que la caja sea demasiado pequeña
    if term_cols < 20: term_cols = 20
    
    # Dibujo del gato pequeño centrado
    small_cat = [
        r"  |\__/,|   (`\ ",
        r" |_ _  |.--.) )",
        r" ( T   )     /",
        r"(((^_((_((____/"
    ]
    
    border_top    = f"{C_CYAN}╔{'═' * (term_cols - 2)}╗{RESET_COLOR}"
    middle_empty  = f"{C_CYAN}║{' ' * (term_cols - 2)}║{RESET_COLOR}"
    
    print(border_top)
    print(middle_empty)
    
    # Dibujar el gato dentro de la caja (solo si cabe)
    for line in small_cat:
        if len(line) < term_cols - 4:
            padding = (term_cols - len(line) - 2) // 2
            print(f"{C_CYAN}║{RESET_COLOR}{' ' * padding}{C_BOLD}{C_GRAY}{line}{RESET_COLOR}{' ' * (term_cols - len(line) - padding - 2)}{C_CYAN}║{RESET_COLOR}")
    
    print(middle_empty)
    
    # Título y subtítulo (truncar si es necesario)
    max_text_w = term_cols - 6
    
    clean_title = title[:max_text_w]
    t_padding = max(0, (term_cols - len(clean_title) - 2) // 2)
    print(f"{C_CYAN}║{RESET_COLOR}{' ' * t_padding}{C_BOLD}{C_GREEN}{clean_title}{RESET_COLOR}{' ' * (term_cols - len(clean_title) - t_padding - 2)}{C_CYAN}║{RESET_COLOR}")
    
    if subtitle:
        clean_sub = subtitle[:max_text_w]
        s_padding = max(0, (term_cols - len(clean_sub) - 2) // 2)
        print(f"{C_CYAN}║{RESET_COLOR}{' ' * s_padding}{C_GRAY}{clean_sub}{RESET_COLOR}{' ' * (term_cols - len(clean_sub) - s_padding - 2)}{C_CYAN}║{RESET_COLOR}")
        
    print(middle_empty)
    print(f"{C_CYAN}╚{'═' * (term_cols - 2)}╝{RESET_COLOR}")
# ── Arte ASCII Gigante (Cabecera) ───────────────────────────────────────────

def show_cat_animation():
    """Pequeña animación de un gato negro caminando por la pantalla."""
    clear_console()
    draw_box_title("PREPARANDO MOTORES...", "Cargando componentes visuales")
    print("\n" * 3)
    
    cat_frames = [
        [
            r"   |\__/,|   (`\ ",
            r" |_ _  |.--.) )",
            r" ( T   )     /",
            r"(((^_((_((____/"
        ],
        [
            r"   |\__/,|   (`\ ",
            r" |_ o  |.--.) )",
            r" ( T   )     /",
            r" ((^_((_((____/",
            r'  "  "'
        ]
    ]
    
    term_cols = os.get_terminal_size().columns
    for i in range(0, term_cols - 20, 2):
        sys.stdout.write(CURSOR_HOME)
        # Re-dibujar el titulo para que no desaparezca (sin el gato gigante aquí)
        draw_box_title("PREPARANDO REPRODUCCIÓN...", "Nicolas Romero (CoralGamer) presenta", show_giant_cat=False)
        
        # Calcular posición del gato
        frame = cat_frames[(i // 4) % 2]
        print("\n" * 5)
        for line in frame:
            sys.stdout.write(f"{' ' * i}{C_BOLD}{C_GRAY}{line}{RESET_COLOR}\n")
        
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(0.5)

def print_info(video_path: str, info: dict) -> None:
    """Muestra la información del video en la terminal con diseño premium."""
    dur   = int(info["duration_s"])
    mins  = dur // 60
    secs  = dur % 60
    
    term_cols = os.get_terminal_size().columns
    clear_console()
    draw_box_title("DETALLES DEL VIDEO", "Analizando metadatos del archivo")
    
    print(f"\n  {C_YELLOW}╔═══════════════════ Datos Técnicos ═══════════════════╗{RESET_COLOR}")
    print(f"  {C_CYAN}║{RESET_COLOR}  {C_BOLD}Archivo{RESET_COLOR}      : {os.path.basename(video_path)}")
    print(f"  {C_CYAN}║{RESET_COLOR}  {C_BOLD}Resolución{RESET_COLOR}   : {info['width_px']} x {info['height_px']} px")
    print(f"  {C_CYAN}║{RESET_COLOR}  {C_BOLD}FPS{RESET_COLOR}          : {info['fps']:.2f}")
    print(f"  {C_CYAN}║{RESET_COLOR}  {C_BOLD}Duración{RESET_COLOR}     : {mins:02d}:{secs:02d} ({info['total_frames']} cuadros)")
    print(f"  {C_YELLOW}╚══════════════════════════════════════════════════════╝{RESET_COLOR}\n")


# ── Conversor de Cuadros (Frames) ─────────────────────────────────────────────

def frame_to_ascii_nocolor(frame, width: int) -> str:
    """Convierte un cuadro a ASCII sin color (más rápido)."""
    height = max(1, int(frame.shape[0] * width / frame.shape[1] / 2))
    resized = cv2.resize(frame, (width, height))
    gray    = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    n_chars = len(ASCII_CHARS) - 1
    lines = []
    for row in gray:
        line = "".join(ASCII_CHARS[int(p / 255.0 * n_chars)] for p in row)
        lines.append(line)
    return "\n".join(lines)


def frame_to_ascii_color(frame, width: int) -> str:
    """Convierte un cuadro a arte ASCII en color ANSI de 24 bits (vectorizado con numpy)."""
    height = max(1, int(frame.shape[0] * width / frame.shape[1] / 2))
    resized     = cv2.resize(frame, (width, height))
    resized_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

    r = resized_rgb[:, :, 0].astype(np.float32)
    g = resized_rgb[:, :, 1].astype(np.float32)
    b = resized_rgb[:, :, 2].astype(np.float32)

    brightness   = 0.299 * r + 0.587 * g + 0.114 * b
    char_indices = np.clip(
        (brightness / 255.0 * (len(ASCII_CHARS) - 1)).astype(np.int32),
        0, len(ASCII_CHARS) - 1
    )
    char_map = _CHARS_ARRAY[char_indices]

    lines = []
    for row_i in range(height):
        parts = []
        for col_i in range(width):
            rv = int(resized_rgb[row_i, col_i, 0])
            gv = int(resized_rgb[row_i, col_i, 1])
            bv = int(resized_rgb[row_i, col_i, 2])
            ch = char_map[row_i, col_i]
            parts.append(f"\033[38;2;{rv};{gv};{bv}m{ch}")
        parts.append(RESET_COLOR)
        lines.append("".join(parts))
    return "\n".join(lines)


# ── Hilo Decodificador en Segundo Plano ───────────────────────────────────────

def _frame_decoder(
    cap: cv2.VideoCapture,
    frame_queue: Queue,
    stop_event: threading.Event,
    skip: int
) -> None:
    """Hilo trabajador: lee cuadros del video hacia la cola saltando cuadros si se solicita."""
    frame_idx = 0
    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break

        # Saltar cuadro si se solicita (para acelerar en PCs lentas)
        if skip > 1 and frame_idx % skip != 0:
            frame_idx += 1
            continue

        frame_idx += 1
        while not stop_event.is_set():
            try:
                frame_queue.put(frame, timeout=0.05)
                break
            except Exception:
                pass

    frame_queue.put(None)  # Centinela de fin


# ── Motor de Reproducción ─────────────────────────────────────────────────────

def play_video(
    video_path : str,
    width      : int  = None,
    use_color  : bool = False,
    skip       : int  = 1,
    loop       : bool = False,
    fit_screen : bool = True,
) -> None:
    """Motor principal de reproducción de video ASCII."""
    if not os.path.exists(video_path):
        print(f"{C_RED}[ERROR]{RESET_COLOR} Archivo no encontrado: '{video_path}'")
        sys.exit(1)

    enable_ansi_windows()
    converter = frame_to_ascii_color if use_color else frame_to_ascii_nocolor

    play_count = 0
    while True:
        play_count += 1
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"{C_RED}[ERROR]{RESET_COLOR} No se pudo abrir el video.")
            sys.exit(1)

        info        = get_video_info(cap)
        fps         = info["fps"] if info["fps"] > 0 else 30.0
        frame_delay = (1.0 / fps) * skip
        
        # Relación de aspecto original del video
        video_ar = info["width_px"] / info["height_px"]

        if play_count == 1:
            print_info(video_path, info)
            mode_str = f"{C_GREEN}COLOR (ANSI 24-bit){RESET_COLOR}" if use_color else f"{C_GRAY}BLANCO Y NEGRO{RESET_COLOR}"
            print(f"  {C_BOLD}Modo{RESET_COLOR}      : {mode_str}")
            print(f"  {C_BOLD}Ajuste{RESET_COLOR}    : {'Automático (Pantalla)' if fit_screen else f'{width} chars'}")
            print(f"  {C_BOLD}Salto{RESET_COLOR}     : cada {skip} cuadros")
            print(f"  {C_BOLD}Bucle{RESET_COLOR}     : {'Sí' if loop else 'No'}")
            print(f"\n{C_YELLOW}Iniciando animación de carga...{RESET_COLOR}")
            time.sleep(1.5)
            show_cat_animation()

        # Decodificador en segundo plano
        frame_queue = Queue(maxsize=8)
        stop_event  = threading.Event()
        decoder     = threading.Thread(
            target=_frame_decoder,
            args=(cap, frame_queue, stop_event, skip),
            daemon=True
        )
        decoder.start()

        # Configuración de terminal
        sys.stdout.write(HIDE_CURSOR)
        sys.stdout.write(CLEAR_SCREEN)
        sys.stdout.flush()

        frame_count   = 0
        total_frames  = max(1, info["total_frames"] // skip)

        try:
            while True:
                t_start = time.perf_counter()

                try:
                    frame = frame_queue.get(timeout=2.0)
                except Empty:
                    break

                if frame is None:
                    break

                frame_count += 1
                
                # Calcular dimensiones dinámicas
                term_size = os.get_terminal_size()
                tw, th = term_size.columns, term_size.lines
                
                if fit_screen:
                    available_h = max(1, th - 2)
                    available_w = tw
                    w_from_h = int(available_h * video_ar * 2.0)
                    current_width = min(available_w, w_from_h)
                else:
                    current_width = width if width else 120

                ascii_art = converter(frame, current_width)

                # Renderizado
                sys.stdout.write(CURSOR_HOME)
                sys.stdout.write(ascii_art)

                # Barra de estado (siempre al final)
                progress = frame_count / total_frames
                bar_len  = max(10, tw - 45) # Barra dinámica
                filled   = int(bar_len * progress)
                bar      = f"{C_GREEN}{'█' * filled}{RESET_COLOR}{C_GRAY}{'░' * (bar_len - filled)}{RESET_COLOR}"
                loop_info = f" | Bucle #{play_count}" if loop else ""
                
                # Posicionar la barra al final de la terminal para evitar parpadeos
                sys.stdout.write(f"\033[{th};1H") 
                sys.stdout.write(
                    f"{C_CYAN}║{RESET_COLOR} [{bar}] "
                    f"{C_BOLD}{frame_count}/{total_frames}{RESET_COLOR}{loop_info} | {C_RED}Ctrl+C{RESET_COLOR}"
                )
                sys.stdout.flush()

                # Temporización precisa
                elapsed    = time.perf_counter() - t_start
                sleep_time = frame_delay - elapsed
                if sleep_time > 0:
                    time.sleep(sleep_time)

        except KeyboardInterrupt:
            stop_event.set()
            raise

        finally:
            stop_event.set()
            decoder.join(timeout=2.0)
            cap.release()

        if not loop:
            break

    # Restaurar terminal
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.write(RESET_COLOR)
    sys.stdout.write(f"\n\n{C_GREEN}[INFO]{RESET_COLOR} Reproducción finalizada.\n")
    sys.stdout.flush()


# ── Analizador de Argumentos CLI ──────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog        = "ASCII_v5_ultimate_ES.py",
        description = "ASCII Art Video Player - Edición Ultimate",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Ejemplos de uso:
  python ASCII_v5_ultimate_ES.py vid.mp4
  python ASCII_v5_ultimate_ES.py vid.mp4 --color --width 100
  python ASCII_v5_ultimate_ES.py vid.mp4 --no-fit --width 140 --loop
  python ASCII_v5_ultimate_ES.py vid.mp4 --color --skip 2
  python ASCII_v5_ultimate_ES.py vid.mp4 --info
"""
    )

    parser.add_argument(
        "video",
        nargs   = "?",
        default = None,
        help    = "Ruta al archivo de video (mp4, avi, mkv, etc.)"
    )
    parser.add_argument(
        "--width", "-w",
        type    = int,
        default = None,
        help    = "Ancho fijo en caracteres (desactiva el ajuste automático)"
    )

    color_group = parser.add_mutually_exclusive_group()
    color_group.add_argument(
        "--color", "-c",
        action  = "store_true",
        default = False,
        help    = "Activa color ANSI 24-bit"
    )
    color_group.add_argument(
        "--no-color",
        action  = "store_true",
        default = False,
        help    = "Fuerza el modo blanco y negro"
    )

    parser.add_argument(
        "--no-fit",
        action  = "store_false",
        dest    = "fit",
        default = True,
        help    = "Desactiva el ajuste automático al tamaño de la ventana"
    )

    parser.add_argument(
        "--skip", "-s",
        type    = int,
        default = 1,
        metavar = "N",
        help    = "Renderiza cada N cuadros"
    )
    parser.add_argument(
        "--loop", "-l",
        action  = "store_true",
        default = False,
        help    = "Repite el video continuamente"
    )
    parser.add_argument(
        "--info", "-i",
        action  = "store_true",
        default = False,
        help    = "Muestra solo la info del video"
    )

    return parser


# ── Punto de Entrada ─────────────────────────────────────────────────────────
def main() -> None:
    enable_ansi_windows()
    parser = build_parser()
    args   = parser.parse_args()

    # Si no hay argumentos, entrar en modo interactivo
    if args.video is None:
        clear_console()
        draw_box_title("ASCII VIDEO PLAYER v5", "Versión actualizada y traducida por CoralGamer")
        
        print(f"\n  {C_GRAY}Para ver todas las opciones: {C_YELLOW}python ASCII_v5_ultimate_ES.py --help{RESET_COLOR}\n")

        args.video = input(f"  {C_BOLD}{C_GREEN}»{RESET_COLOR} Introduce la ruta del video: ").strip().strip('"')
        if not args.video:
            print(f"  {C_RED}[ERROR]{RESET_COLOR} La ruta del video no puede estar vacía.")
            sys.exit(1)

        color_input = input(f"  {C_BOLD}{C_GREEN}»{RESET_COLOR} ¿Activar color? (s/N): ").strip().lower()
        args.color  = color_input == "s"

        fit_input = input(f"  {C_BOLD}{C_GREEN}»{RESET_COLOR} ¿Ajustar automáticamente a la terminal? (S/n): ").strip().lower()
        args.fit   = fit_input != "n"

        if not args.fit:
            term_cols = os.get_terminal_size().columns
            try:
                w = input(f"  {C_BOLD}{C_GREEN}»{RESET_COLOR} Ancho de salida (default 120, terminal={term_cols}): ").strip()
                args.width = int(w) if w else 120
            except ValueError:
                args.width = 120

        try:
            s = input(f"  {C_BOLD}{C_GREEN}»{RESET_COLOR} Saltar cada N cuadros (default 1): ").strip()
            args.skip = int(s) if s else 1
        except ValueError:
            args.skip = 1

        loop_input = input(f"  {C_BOLD}{C_GREEN}»{RESET_COLOR} ¿Repetir video? (s/N): ").strip().lower()
        args.loop   = loop_input == "s"

    # Si se especifica un ancho manualmente, desactivamos el fit automático por defecto
    if args.width is not None:
        args.fit = False

    # Validación
    if args.skip < 1:
        args.skip = 1

    # Modo solo información
    if args.info:
        if not os.path.exists(args.video):
            print(f"{C_RED}[ERROR]{RESET_COLOR} Archivo no encontrado: '{args.video}'")
            sys.exit(1)
        cap  = cv2.VideoCapture(args.video)
        info = get_video_info(cap)
        cap.release()
        print_info(args.video, info)
        return

    # Reproducir video
    try:
        play_video(
            video_path = args.video,
            width      = args.width,
            use_color  = args.color,
            skip       = args.skip,
            loop       = args.loop,
            fit_screen = args.fit
        )
    except KeyboardInterrupt:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.write(RESET_COLOR)
        print(f"\n\n{C_YELLOW}[INFO]{RESET_COLOR} Detenido por el usuario.\n")


if __name__ == "__main__":
    main()
