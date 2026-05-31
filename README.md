# 🎬 ASCII Player Video Creator — Official V5 Release

<div align="center">
  <img src="https://raw.githubusercontent.com/CoralGamer/ACSII-Video-Convertor---Web-Free/main/assets/readme/banner.png" alt="ASCII Player Creator Banner" width="100%" style="border-radius: 12px; margin-bottom: 20px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);" />

  <p><strong>A professional text-based (CLI) video rendering and creation suite that allows you to play, convert, and export any video file into highly structured retro ASCII art terminal animations, with full proportional auto-fit and multi-language support.</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Support" />
    <img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV Support" />
    <img src="https://img.shields.io/badge/NumPy-1.20+-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy Support" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License MIT" />
  </p>

  <p>
    <iframe src="https://github.com/sponsors/CoralGamer/button" title="Sponsor CoralGamer" height="32" width="114" style="border: 0; border-radius: 6px;"></iframe>
  </p>
</div>

---

## ⚡ Showcase & Visual Tour

<table align="center" style="width: 100%; text-align: center; border-collapse: collapse;">
  <tr>
    <td width="50%"><strong>🌀 Proportional 3D Canvas rendering</strong></td>
    <td width="50%"><strong>⚡ CRT Phosphor Retro Visualizer</strong></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/CoralGamer/ACSII-Video-Convertor---Web-Free/main/assets/readme/matrix-neon-render.png" alt="Matrix Neon Proportional Render" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);" /></td>
    <td><img src="https://raw.githubusercontent.com/CoralGamer/ACSII-Video-Convertor---Web-Free/main/assets/readme/3d-cube-render.png" alt="CRT Phosphor Visualizer" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);" /></td>
  </tr>
</table>

---

## ✨ Key Features in V5

- **📽️ MP4 Export Engine**: Convert any local video file into an ASCII-styled MP4. Choose between compiling the final video with customizable backgrounds or keeping every individual high-definition PNG frame.
- **🌍 Multi-Language CLI**: Completely interactive terminal interface supporting six languages on startup: **English, Spanish, French, Portuguese, German, and Indonesian**.
- **🖥️ Proportional Auto-Fit**: Real-time terminal scaling engine that recalculates the rows/columns dynamically to fit your console window (width & height) perfectly while preserving aspect ratio.
- **🎨 Infinite Background Customization**: Adjust your exports with presets (Deep Black, Solid White, Classic Blue) or supply any Custom Hex code (`#120a2a` etc.) for a premium cyberpunk or vaporwave finish.
- **🌈 24-bit ANSI Terminal Colors**: High-fidelity character coloring for a breathtaking command-line cinema experience.
- **⚡ Async Frame Decoding**: Background multi-threaded decoding and vectorized processing to achieve smooth, lag-free playback and rendering.
- **🖋️ Deep Shading Characters**: Expanded, mathematically balanced character density set for ultra-detailed shadows and sharp contrast highlights.
- **📱 Android Termux Compatibility**: Optimizations included to run the command-line suite directly on mobile devices using Termux.

---

## 🛠️ Requirements & Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/CoralGamer/ASCII-Video-Player.git
   cd ASCII-Video-Player
   ```

2. Install the necessary lightweight dependencies using pip:
   ```bash
   pip install opencv-python numpy Pillow
   ```

---

## 🚀 How to Run

Simply run the script from your terminal:

```bash
python ASCII_v5_official.py
```

### Guided Workflow:
1. **Language Selection**: Choose your preferred language.
2. **Video Path Selection**: Type the path to your video file.
3. **Rendering Parameters**: Adjust size (columns), skip frames (for speedups), and select color mode (Grayscale / Colors).
4. **Interactive Playback**: Watch the live preview render directly inside your command line terminal.
5. **Export Setup**: Save your result to an MP4 video or export frame-by-frame PNG folders.
6. **Continuous Cycle**: Run another video conversion immediately without restarting the program!

---

## 🌐 Prefer a Web Interface?

We have built a premium, server-free, 100% client-side web application! You can upload videos and process them with Floyd-Steinberg dithering, custom palette shaders, and even generate ASCII animations from text prompts:
👉 **[Launch the Web Application Suite](https://coralgamer.github.io/ACSII-Video-Convertor---Web-Free/)**

---

## 💡 Contributors & Credits

- **Original Core Concept**: [stepanussaruran](https://github.com/stepanussaruran)
- **V5 Architecture & Export Core**: Nicolas Romero ([coralgamer](https://github.com/nicolas-romero))

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
*Language Versions: [Español](README_ES.md) | [Français](README_FR.md) | [Português](README_PT.md) | [Deutsch](README_DE.md) | [Indonesian](README_ID.md)*
