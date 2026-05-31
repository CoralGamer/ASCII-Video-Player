# 🎬 ASCII Player Video Creator — Lanzamiento Oficial V5

<div align="center">
  <img src="https://raw.githubusercontent.com/CoralGamer/ACSII-Video-Convertor---Web-Free/main/assets/readme/banner.png" alt="ASCII Player Creator Banner" width="100%" style="border-radius: 12px; margin-bottom: 20px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);" />

  <p><strong>Una suite profesional de renderizado y creación de vídeo basada en terminal (CLI) que te permite reproducir, convertir y exportar cualquier archivo de vídeo en animaciones de caracteres ASCII retro, con auto-ajuste de proporciones en tiempo real y soporte multi-idioma interactivo.</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Soporte Python" />
    <img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="Soporte OpenCV" />
    <img src="https://img.shields.io/badge/NumPy-1.20+-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Soporte NumPy" />
    <img src="https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge" alt="Licencia MIT" />
  </p>

  <p>
    <iframe src="https://github.com/sponsors/CoralGamer/button" title="Sponsor CoralGamer" height="32" width="114" style="border: 0; border-radius: 6px;"></iframe>
  </p>
</div>

---

## ⚡ Exhibición Visual & Demostración

<table align="center" style="width: 100%; text-align: center; border-collapse: collapse;">
  <tr>
    <td width="50%"><strong>🌀 Renderizado de Canvas Proporcional</strong></td>
    <td width="50%"><strong>⚡ Visualizador CRT Fósforo Verde Retro</strong></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/CoralGamer/ACSII-Video-Convertor---Web-Free/main/assets/readme/matrix-neon-render.png" alt="Render Proporcional de Matriz" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);" /></td>
    <td><img src="https://raw.githubusercontent.com/CoralGamer/ACSII-Video-Convertor---Web-Free/main/assets/readme/3d-cube-render.png" alt="Visualizador CRT Fósforo Verde" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);" /></td>
  </tr>
</table>

---

## ✨ Características Clave de la Versión V5

- **📽️ Motor de Exportación MP4**: Convierte cualquier video local en un MP4 estilizado en arte ASCII de texto. Permite elegir entre compilar el vídeo final con fondos ajustables o exportar cada frame individual en PNG de alta definición.
- **🌍 CLI Multilingüe Interactivo**: Interfaz guiada por terminal con soporte para seis idiomas en el arranque: **Español, Inglés, Francés, Portugués, Alemán e Indonesio**.
- **🖥️ Auto-Ajuste Proporcional Inteligente**: Motor de escalado dinámico en consola que recalcula columnas y filas en tiempo real al cambiar el tamaño de tu ventana de terminal, manteniendo siempre la relación de aspecto del vídeo original.
- **🎨 Colores de Fondo Infinitos**: Personaliza tu renderizado de exportación con ajustes preestablecidos (Negro Absoluto, Blanco Sólido, Azul Clásico) o escribe cualquier código Hexadecimal personalizado (`#150e2a` etc.) para lograr acabados cyberpunk o synthwave de alto nivel.
- **🌈 Color ANSI de 24 bits**: Coloreado de caracteres RGB de alta fidelidad directamente en la consola para una experiencia cinematográfica retro espectacular.
- **⚡ Decodificación de Cuadros Asíncrona**: Decodificación multi-hilo en segundo plano y procesamiento vectorizado para garantizar un frame-rate fluido y libre de latencia en la terminal.
- **🖋️ Set de Caracteres de Alta Densidad**: Conjunto de sombreadores matemáticamente equilibrado para sombras profundas y detalles de contorno ultra-precisos.
- **📱 Compatibilidad con Android Termux**: Optimizaciones incorporadas para correr la suite CLI desde teléfonos o tablets Android a través de Termux de manera nativa.

---

## 🛠️ Instalación y Requisitos

1. Clona el repositorio y navega al directorio del proyecto:
   ```bash
   git clone https://github.com/CoralGamer/ASCII-Video-Player.git
   cd ASCII-Video-Player
   ```

2. Instala las dependencias necesarias de Python mediante pip:
   ```bash
   pip install opencv-python numpy Pillow
   ```

---

## 🚀 Cómo Ejecutar

Simplemente lanza el script principal en tu terminal de comandos:

```bash
python ASCII_v5_official.py
```

### Flujo Guiado Interactivo:
1. **Selección de Idioma**: Elige el idioma de tu preferencia para la sesión.
2. **Carga del Vídeo**: Escribe la ruta local del archivo de vídeo a procesar.
3. **Parámetros del Render**: Configura el ancho (columnas), el salto de cuadros para acelerar el renderizado, y el modo de color (Blanco y Negro / Colores ANSI).
4. **Reproducción en Vivo**: Disfruta de la previsualización directa y fluida del vídeo renderizado en caracteres dentro de tu terminal.
5. **Configuración de Exportación**: Elige si deseas guardar el resultado en un vídeo MP4 o generar carpetas con frames PNG secuenciales.
6. **Ciclo Continuo**: ¡Procesa nuevos vídeos al instante sin tener que reiniciar el programa!

---

## 🌐 ¿Prefieres usar una Interfaz Web?

Hemos desarrollado una suite web premium, ultra-rápida y 100% en cliente (sin servidores). Puedes procesar tus vídeos con sombreadores de paletas de colores, algoritmos avanzados de difuminado Floyd-Steinberg, e incluso generar arte ASCII dinámico mediante prompts semánticos de Inteligencia Artificial:
👉 **[Lanzar la Suite Web en Vivo](https://coralgamer.github.io/ACSII-Video-Convertor---Web-Free/)**

---

## 💡 Contribuidores & Créditos

- **Concepto del Núcleo Original**: [stepanussaruran](https://github.com/stepanussaruran)
- **Arquitectura V5 y Core del Exportador**: Nicolas Romero ([coralgamer](https://github.com/nicolas-romero))

---

## ⚖️ Licencia

Distribuido bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más información.

---
*Otros Idiomas: [English](README.md) | [Français](README_FR.md) | [Português](README_PT.md) | [Deutsch](README_DE.md) | [Indonesian](README_ID.md)*
