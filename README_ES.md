# 🎬 ASCII Player Video Creator — El Motor Definitivo de Arte Retro

<div align="center">
  <img src="web-app/assets/readme/banner.png" alt="ASCII Player Creator Banner" width="100%" style="border-radius: 12px; margin-bottom: 20px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);" />

  <p><strong>Una suite de renderizado de alto rendimiento para doble entorno que consta de un motor CLI optimizado en Python 3 y una aplicación web premium de cliente en JavaScript Vanila. Convierte cualquier vídeo local o genera espectaculares animaciones procedimentales en 3D a partir de sencillos prompts de texto en un impresionante arte de caracteres ASCII al estilo de terminal retro a más de 60 FPS.</strong></p>

  <p>
    <a href="https://coralgamer.github.io/ACSII-Video-Convertor---Web-Free/"><img src="https://img.shields.io/badge/Demo_En_Vivo-Probar_Web_App-00f2fe?style=for-the-badge&logo=google-chrome&logoColor=black" alt="Probar Demo" /></a>
    <a href="https://github.com/CoralGamer/ACSII-Video-Convertor---Web-Free/stargazers"><img src="https://img.shields.io/github/stars/CoralGamer/ACSII-Video-Convertor---Web-Free?style=for-the-badge&logo=github&color=yellow" alt="Estrellas en GitHub" /></a>
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Soporte Python" />
    <img src="https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge" alt="Licencia MIT" />
  </p>

  <p>
    <a href="https://github.com/sponsors/CoralGamer">
      <img src="https://img.shields.io/badge/Sponsor-CoralGamer-ea4aaa?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="Badge de Patrocinador GitHub" />
    </a>
  </p>

  <details>
    <summary>Haz clic aquí para copiar el código HTML del iframe de patrocinio</summary>
    <pre><code>&lt;iframe src="https://github.com/sponsors/CoralGamer/button" title="Sponsor CoralGamer" height="32" width="114" style="border: 0; border-radius: 6px;"&gt;&lt;/iframe&gt;</code></pre>
  </details>
</div>

---

## ⚡ Exhibición Visual & Demostración

Descubre los componentes visuales de diseño moderno y estilizado que dan vida a nuestra interfaz ASCII:

<table align="center" style="width: 100%; text-align: center; border-collapse: collapse;">
  <tr>
    <td width="50%"><strong>🖥️ Interfaz Avanzada de Renderizado (Dashboard)</strong></td>
    <td width="50%"><strong>🎨 Mapeo de Color Real RGB y Caracteres (Dithering)</strong></td>
  </tr>
  <tr>
    <td><img src="web-app/assets/readme/app-interface.png" alt="Panel de Control Web" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
    <td><img src="web-app/assets/readme/dithering-color-render.png" alt="Difuminado en Color Real RGB" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
  </tr>
  <tr>
    <td colspan="2"><br/></td>
  </tr>
  <tr>
    <td width="50%"><strong>🤖 Generador Procedimental por Prompts (IA Engine)</strong></td>
    <td width="50%"><strong>🔋 Proyecciones 3D CRT Fósforo Verde (3D Engine)</strong></td>
  </tr>
  <tr>
    <td><img src="web-app/assets/readme/ai-prompt-generator.png" alt="Generador de IA a ASCII en Vivo" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
    <td><img src="web-app/assets/readme/3d-cube-render.png" alt="Cubo Giratorio 3D Fósforo Verde" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
  </tr>
  <tr>
    <td colspan="2"><br/></td>
  </tr>
  <tr>
    <td width="50%"><strong>📽️ Degradados Cyberpunk y Matrix Lluvia (Temas)</strong></td>
    <td width="50%"><strong>⭐ Sincronización y Resplandor de Valoración (GitHub Sync)</strong></td>
  </tr>
  <tr>
    <td><img src="web-app/assets/readme/matrix-neon-render.png" alt="Renders de Temas Matrix y Neón" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
    <td><img src="web-app/assets/readme/github-stars-sync.png" alt="Módulo de Sincronización GitHub Stars" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
  </tr>
</table>

> [!NOTE]
> *Asegúrate de hacer commit y push a todos los archivos dentro de `web-app/assets/readme/` en tu repositorio remoto para que GitHub pueda leer y mostrar estos recursos locales correctamente.*

---

## 🛠️ Pilas Tecnológicas & Arquitectura

Esta suite saca partido de dos arquitecturas tecnológicas independientes adaptadas al máximo rendimiento de ejecución:

### 1. El Motor CLI en Python (`ASCII_v5_official.py`)
Una veloz utilidad de línea de comandos multihilo optimizada para el procesamiento de vídeo local y renderizado por lotes en terminal.
* **Tecnología Principal**: `Python 3.8+`
* **Decodificación de Vídeo y Operaciones Matriciales**: `OpenCV (opencv-python)` y `NumPy`
* **Cuantización de Imágenes y Slices**: `Pillow (PIL)`
* **Características Clave**:
  * **Auto-Ajuste Dinámico de Terminal**: Hook dinámico en consola que monitorea en tiempo real las dimensiones del buffer del sistema y recalcula filas y columnas al redimensionar la ventana de comandos, manteniendo la proporción exacta del vídeo original.
  * **Decodificación Asíncrona Multi-hilo**: Utiliza hilos de cola en Python para leer, decodificar y vectorizar matrices de vídeo en segundo plano, evitando tirones en la reproducción interactiva.
  * **Color Real ANSI de 24 bits**: Inyección directa de bytes RGB sobre el buffer de la terminal del sistema (POSIX/Windows).
  * **Motor de Exportación MP4 Personalizable**: Elige entre colores de fondo sólidos (Negro Profundo, Blanco Puro, Azul Clásico) o cualquier color hexadecimal personalizado `#hex`, compilando el render final localmente o conservando los fotogramas PNG individuales en alta definición.
  * **Soporte Completo para Android Termux**: Probado y optimizado para ejecutarse en terminales móviles sin problemas de rendimiento.

### 2. La Aplicación Web del Cliente (`web-app/`)
Una espectacular e interactiva web de una sola página, sin servidor y que corre a más de 60 fotogramas por segundo completamente en el navegador del usuario.
* **Tecnología Principal**: `HTML5 Canvas 2D Context`, `Vanilla JavaScript ES6+` (Cero Frameworks, Cero dependencias de NPM)
* **Estilizado**: `CSS3 Vanila` con propiedades dinámicas personalizadas (variables CSS) para un diseño futurista neón y acabados de glassmorphism premium.
* **Pipeline de IA Visual Avanzado**:
  * **Smart Prompt Augmentation**: Enriquece semánticamente los prompts del usuario con descriptores de renderizado y calidad profesional (`highly detailed`, `sharp focus`, `vibrant colors`, `4k resolution`) de forma dinámica, evitando duplicados.
  * **Integración API de IA Text-to-Image / WebGPU**: Obtiene imágenes generativas de alta definición usando arquitecturas de difusión avanzadas del modelo `flux`, escalando a `768x768` píxeles con mecanismos de fallbacks robustos si el modelo no está disponible.
  * **Núcleo de Post-Procesamiento de Imágenes en 3 Etapas**:
    1. *Auto-Contraste*: Normaliza histogramas espaciales aplicando un clipping del 1% para maximizar el rango dinámico.
    2. *Unsharp Mask*: Emplea una convolución por sustracción de kernel gaussiano 3x3 de paso alto restado para perfilar detalles finos.
    3. *Edge Enhancement*: Calcula gradientes de Sobel para dibujar contornos nítidos y limpios que faciliten el mapeo ASCII de caracteres.
  * **Campo de Deformación Orgánico Multicapa**: Algoritmo matemático de deformación y desplazamiento por ruido que superpone 4 capas independientes (marea baja, corrientes cruzadas de frecuencia media, turbulencia de alta frecuencia y vórtice de succión central), complementado con un pulso sinusoidal de respiración y zoom (1.5%).
  * **Interpolación Bilineal**: Mapea sub-píxeles sobre sus 4 vecinos espaciales eliminando el aliasing o dientes de sierra característicos del muestreo simple por vecino más cercano.
  * **Sombreador ASCII Avanzado**: Mapeo tonal con corrección gamma, multiplicador de saturación de 1.35x para colores neón vibrantes, y brillo tenue azulado sobre caracteres casi negros para que las texturas oscuras no pierdan volumen.
* **Grabador y Exportador Multiformato**: Utiliza la API `MediaRecorder` y `captureStream()` del canvas HTML5 para compilar y descargar vídeos finalizados con audio sincronizado (MP4, WebM, MKV, MOV, AVI) directamente en la máquina local.
* **Módulo de Sincronización GitHub**: Tarjeta interactiva conectada a la API oficial con almacenamiento en caché `localStorage` (cache-first) para respetar límites de cuota, activando destellos de confirmación visuales al recibir el soporte del usuario.

---

## 📐 Fundamentos Matemáticos

Nuestra suite web y de consola destaca por la aplicación de ecuaciones de precisión visual:

### 1. Luminancia Relativa (Norma NTSC/BT.709)
Convertimos los canales de color a un mapa de escala de grises ponderado adaptado a la respuesta del ojo humano:
$$Y = 0.2126 \cdot R + 0.7152 \cdot G + 0.0722 \cdot B$$

### 2. Difusión de Error Floyd-Steinberg
Para suavizar transiciones tonales y evitar el efecto banding, repartimos el error de cuantización entre el píxel procesado y el caracter ASCII en una matriz espacial de pesos fraccionarios:
$$\text{Error} = Y_{\text{píxel}} - \text{Densidad}_{\text{caracter}}$$
$$\text{Grilla de Dispersión:} \quad (X+1, Y) \leftarrow \frac{7}{16}, \quad (X-1, Y+1) \leftarrow \frac{3}{16}, \quad (X, Y+1) \leftarrow \frac{5}{16}, \quad (X+1, Y+1) \leftarrow \frac{1}{16}$$

### 3. Muestreo por Interpolación Bilineal
Durante las deformaciones matemáticas por fluidos, las coordenadas en punto flotante se ponderan de manera contigua para asegurar transformaciones súper fluidas y sin pixelación ruidosa:
$$f(x, y) \approx (1 - \Delta x)(1 - \Delta y) \cdot Q_{11} + \Delta x(1 - \Delta y) \cdot Q_{21} + (1 - \Delta x)\Delta y \cdot Q_{12} + \Delta x \Delta y \cdot Q_{22}$$

---

## 🚀 Instalación y Puesta en Marcha

### Ejecución del Motor CLI de Consola (Python)
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/CoralGamer/ASCII-Video-Player.git
   cd ASCII-Video-Player
   ```
2. **Instala dependencias**:
   ```bash
   pip install opencv-python numpy Pillow
   ```
3. **Ejecuta el script principal**:
   ```bash
   python ASCII_v5_official.py
   ```
   *Sigue las instrucciones en tu idioma en pantalla para cargar, visualizar y exportar tus vídeos.*

---

### Ejecución de la Suite de Aplicación Web
Al ser una aplicación 100% de ejecución local en el cliente, iniciarla es inmediato:

#### Método A: Carga Directa
Accede a la carpeta `web-app` y haz doble clic sobre `index.html` para abrirlo en cualquier navegador web moderno.

#### Método B: Servidor de Desarrollo Local (Altamente recomendado para evitar restricciones CORS de archivos locales)
* **Si tienes Python 3**:
  ```bash
  python -m http.server 8000
  ```
* **Si tienes Node.js**:
  ```bash
  npx http-server ./ -p 8000
  ```
Una vez iniciado, visita `http://localhost:8000` en tu navegador.

---

## 🤝 Créditos & Soporte

* **Concepto Original**: [@stepanussaruran](https://github.com/stepanussaruran)
* **Arquitectura V5, Módulo de IA y Desarrollo Web**: Nicolas Romero ([@coralgamer](https://github.com/nicolas-romero))

---

## ⚖️ Licencia

Distribuido bajo la **Licencia MIT**. Consulta [LICENSE](LICENSE) para más información.

---
*Otros Idiomas: [English (Inglés)](README.md) | [Français (Francés)](README_FR.md) | [Português (Portugués)](README_PT.md) | [Deutsch (Alemán)](README_DE.md) | [Indonesian (Indonesio)](README_ID.md)*
