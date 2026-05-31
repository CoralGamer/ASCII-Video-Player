# 🎬 ASCII Player Video Creator — The Ultimate Retro Art Engine

<div align="center">
  <img src="web-app/assets/readme/banner.png" alt="ASCII Player Creator Banner" width="100%" style="border-radius: 12px; margin-bottom: 20px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);" />

  <p><strong>A high-performance, dual-environment rendering suite consisting of an optimized Python 3 CLI engine and a premium Vanilla JS Client-Side Web Application. Convert any local video or generate gorgeous 3D procedural animations from simple text prompts into stunning retro terminal-style ASCII character art at 60+ FPS.</strong></p>

  <p>
    <a href="https://coralgamer.github.io/ACSII-Video-Convertor---Web-Free/"><img src="https://img.shields.io/badge/Live_Demo-Try_Web_App-00f2fe?style=for-the-badge&logo=google-chrome&logoColor=black" alt="Try Demo" /></a>
    <a href="https://github.com/CoralGamer/ACSII-Video-Convertor---Web-Free/stargazers"><img src="https://img.shields.io/github/stars/CoralGamer/ACSII-Video-Convertor---Web-Free?style=for-the-badge&logo=github&color=yellow" alt="GitHub Stars" /></a>
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Support" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License MIT" />
  </p>

  <p>
    <a href="https://github.com/sponsors/CoralGamer">
      <img src="https://img.shields.io/badge/Sponsor-CoralGamer-ea4aaa?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="Sponsor CoralGamer Badge" />
    </a>
  </p>

  <details>
    <summary>Click to copy raw HTML Sponsor Code</summary>
    <pre><code>&lt;iframe src="https://github.com/sponsors/CoralGamer/button" title="Sponsor CoralGamer" height="32" width="114" style="border: 0; border-radius: 6px;"&gt;&lt;/iframe&gt;</code></pre>
  </details>
</div>

---

## ⚡ Showcase & Visual Tour

Discover the modern, beautifully styled visual components that power our ASCII interface:

<table align="center" style="width: 100%; text-align: center; border-collapse: collapse;">
  <tr>
    <td width="50%"><strong>🖥️ Web Application Dashboard</strong></td>
    <td width="50%"><strong>🎨 True Color RGB Dithering</strong></td>
  </tr>
  <tr>
    <td><img src="web-app/assets/readme/app-interface.png" alt="Web Application Dashboard" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
    <td><img src="web-app/assets/readme/dithering-color-render.png" alt="True Color RGB Dithering" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
  </tr>
  <tr>
    <td colspan="2"><br/></td>
  </tr>
  <tr>
    <td width="50%"><strong>🤖 Generative Prompt Engine</strong></td>
    <td width="50%"><strong>🔋 Phosphor Green 3D Retro Render</strong></td>
  </tr>
  <tr>
    <td><img src="web-app/assets/readme/ai-prompt-generator.png" alt="Generative AI to ASCII Output" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
    <td><img src="web-app/assets/readme/3d-cube-render.png" alt="Phosphor Green 3D Rotating Cube" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
  </tr>
  <tr>
    <td colspan="2"><br/></td>
  </tr>
  <tr>
    <td width="50%"><strong>📽️ Interactive Custom Themes (Neon & Matrix)</strong></td>
    <td width="50%"><strong>⭐ Real-Time GitHub Star Tracker</strong></td>
  </tr>
  <tr>
    <td><img src="web-app/assets/readme/matrix-neon-render.png" alt="Matrix and Neon Theme Render" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
    <td><img src="web-app/assets/readme/github-stars-sync.png" alt="GitHub Stargazers Sync" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 100%;" /></td>
  </tr>
</table>

> [!NOTE]
> *Make sure to commit and push all files in `web-app/assets/readme/` to your remote repository so GitHub can display these local assets correctly.*

---

## 🛠️ Technological Stacks & Architecture

This suite leverages two distinct architectural stacks tailored for peak execution performance:

### 1. The Python CLI Engine (`ASCII_v5_official.py`)
A fast, multithreaded command-line utility optimized for local video processing and batch terminal rendering.
* **Core Tech**: `Python 3.8+`
* **Video Decoding & Array Operations**: `OpenCV (opencv-python)` & `NumPy`
* **Image Quantization & Slices**: `Pillow (PIL)`
* **Key Features**:
  * **Dynamic Terminal Auto-Fit**: A custom runtime terminal polling hook that dynamically rescales columns and rows as you resize the console window, maintaining a perfect proportional aspect ratio.
  * **Asynchronous Multi-threaded Decoding**: Uses Python queue threads to fetch, decode, and vectorize image arrays in the background, minimizing playback stutter.
  * **True 24-bit ANSI Character Coloring**: Direct RGB byte projection onto standard POSIX/Windows terminal buffers.
  * **Configurable Background MP4 Export Engine**: Choose from solid color backgrounds (Deep Black, Pure White, Classic Blue) or any custom `#hex` color, compiling the final video locally with standard codec support or preserving raw PNG frames.
  * **Full Android Termux Support**: Fully tested and optimized to run on mobile command lines.

### 2. The Client-Side Web Application (`web-app/`)
A state-of-the-art, highly visual, serverless web app running at 60+ FPS entirely in the client's browser.
* **Core Tech**: `HTML5 Canvas 2D Context`, `Vanilla ES6+ Javascript` (Zero Frameworks, Zero NPM dependencies)
* **Styling**: `Vanilla CSS3` using dynamic custom properties (CSS variables) for modern neon and glassmorphism styling.
* **Advanced Visual AI Pipeline**:
  * **Smart Prompt Augmentation**: Enriches standard user prompts with cinematic and render-quality keywords (`highly detailed`, `sharp focus`, `vibrant colors`, `4k resolution`) dynamically preventing duplicates.
  * **AI Text-to-Image / WebGPU API Integration**: Pulls high-fidelity generated images via advanced `flux` diffusion structures, scaling dynamically to `768x768` pixels with robust fallback models.
  * **3-Stage Image Post-Processing Core**:
    1. *Auto-Contrast*: Normalizes histograms with 1% pixel value clipping to maximize dynamic range.
    2. *Unsharp Mask*: Employs a fast 3x3 high-pass Gaussian kernel subtraction to sharpen outlines.
    3. *Edge Enhancement*: Calculates Sobel gradients to draw clean, distinct outlines for character mapping.
  * **Organic Multilayer Deformation Field**: A custom noise-deforming displacement algorithm that combines 4 distinct waves (low-frequency ocean swell, medium cross-currents, high-frequency turbulence, and rotational vortex center-focused pull) with a global sinusoidal "breathing" zoom effect.
  * **Bilinear Subpixel Interpolation**: Maps sub-pixel coordinates to their four nearest neighbors, removing jagged pixelation artifacts during animated warping.
  * **Advanced Character Shader**: Employs gamma-corrected luminance character mapping, a 1.35x saturation boost multiplier for glowing neon modes, and a faint blue dark-glow overlay on near-black characters to preserve texture visibility.
* **Multi-Format Container Exporter**: Uses HTML5 `Canvas.captureStream()` combined with the browser's native `MediaRecorder` API to export files (MP4, WebM, MKV, MOV, AVI) with synchronized audio directly in the client.
* **GitHub Star Sync System**: Features a custom cache-first Stargazers tracker communicating with the GitHub API (`localStorage` caching to respect rate-limits), triggering a beautiful glowing animation upon interactive endorsement.

---

## 📐 Mathematical Foundations

Our high-fidelity ASCII mapping is backed by rigorous visual equations:

### 1. Relative Luminance (NTSC/BT.709 Spec)
Before mapping characters, pixels are converted to grayscale using weights adjusted for human spectral sensitivity:
$$Y = 0.2126 \cdot R + 0.7152 \cdot G + 0.0722 \cdot B$$

### 2. Floyd-Steinberg Error Diffusion
To eliminate visual banding and preserve light gradients, the quantization error between the target pixel and the available ASCII density step is propagated to adjacent coordinates using fractional spatial weights:
$$\text{Error} = Y_{\text{pixel}} - \text{Density}_{\text{char}}$$
$$\text{Distribution Grid:} \quad (X+1, Y) \leftarrow \frac{7}{16}, \quad (X-1, Y+1) \leftarrow \frac{3}{16}, \quad (X, Y+1) \leftarrow \frac{5}{16}, \quad (X+1, Y+1) \leftarrow \frac{1}{16}$$

### 3. Bilinear Subpixel Sampling
During the dynamic deformation warping, floating-point coordinates are mapped to adjacent integer pixels to guarantee ultra-smooth rendering transitions:
$$f(x, y) \approx (1 - \Delta x)(1 - \Delta y) \cdot Q_{11} + \Delta x(1 - \Delta y) \cdot Q_{21} + (1 - \Delta x)\Delta y \cdot Q_{12} + \Delta x \Delta y \cdot Q_{22}$$

---

## 🚀 Getting Started & Local Execution

### Running the Python CLI Engine
1. **Clone the repository**:
   ```bash
   git clone https://github.com/CoralGamer/ASCII-Video-Player.git
   cd ASCII-Video-Player
   ```
2. **Install OpenCV & dependencies**:
   ```bash
   pip install opencv-python numpy Pillow
   ```
3. **Execute the interactive script**:
   ```bash
   python ASCII_v5_official.py
   ```
   *Follow the multi-language interactive terminal guide to load, play, and export your local files.*

---

### Running the Premium Web Application
Because the web dashboard runs 100% on the client side, launching it is extremely simple:

#### Method A: Direct Launch
Simply navigate into the `web-app` folder and open `index.html` in any modern web browser.

#### Method B: Local Server (Highly Recommended to prevent local CORS security warnings)
* **Using Python 3**:
  ```bash
  python -m http.server 8000
  ```
* **Using Node.js**:
  ```bash
  npx http-server ./ -p 8000
  ```
Once started, visit `http://localhost:8000` to enjoy the premium high-FPS canvas interface.

---

## 🤝 Contributors & Support

* **Original Core Concept**: [@stepanussaruran](https://github.com/stepanussaruran)
* **V5 Architecture, AI Pipeline & Web Core**: Nicolas Romero ([@coralgamer](https://github.com/nicolas-romero))

---

## ⚖️ License

Distributed under the **MIT License**. Check [LICENSE](LICENSE) for full details.

---
*Other Language Variations: [Español (Spanish)](README_ES.md) | [Français (French)](README_FR.md) | [Português (Portuguese)](README_PT.md) | [Deutsch (German)](README_DE.md) | [Indonesian](README_ID.md)*
