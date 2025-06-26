# 🕵️ Steganography Tool - Embed & Extract Hidden Messages

A Python-based GUI application to **embed** and **extract hidden messages** from image or audio files using **LSB (Least Significant Bit) steganography**.

Developed with:
- PySimpleGUI
- Pillow (PIL)
- NumPy
- PyDub
- SciPy

---

## 🔧 Features

- 🔐 Embed secret messages into **images (PNG, JPG)** using LSB encoding
- 🔊 Embed messages into **audio (WAV)** files (optional: implement method)
- 📤 Extract hidden messages from images or audio
- 💾 Save encoded images directly from the app
- 🖥️ Simple and clean **GUI interface**

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rooter09/UrlScanToolKit.git
cd UrlScanToolKit  # Or your tool's folder
```

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate     # On Linux/macOS
.venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Install FFmpeg for Audio Steganography (if using audio)
Download from:
```
https://ffmpeg.org/download.html
```
Add FFmpeg to your system PATH

---

### 🚀 Usage
Run the tool:
```
python your_script_name.py
```
## GUI Options:
- Embed Message: Choose an image/audio file, enter a message, and embed it.
- Extract Message: Select a stego file and extract the hidden message.
- Save Image: Save a selected image with or without modifications.

### 📂 File Types Supported

| File Type     | Embed | Extract |
|---------------|:-----:|:-------:|
| \.png\ / \.jpg\ | ✅   | ✅     |
| \.wav\          | ❌ *(coming soon)* | ❌ *(coming soon)* |

---

## 🛠 Dependencies
See requirements.txt:
```
PySimpleGUI
Pillow
numpy
pydub
scipy

```

### 🧠 How It Works (Image LSB)
- Each pixel's color values (RGB) are slightly modified by replacing the Least Significant Bit with bits of the message.
- A null character '\0' is appended to the message to signal the end during extraction.

### ✅ To-Do / Future Features
- Image steganography
- Audio steganography (embed/extract)
- File encryption support
- - Batch processing

### ⚖️ License
MIT License © 2025 Harsh Sandilya a.k.a rooter09 

### 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change or improve.

---

