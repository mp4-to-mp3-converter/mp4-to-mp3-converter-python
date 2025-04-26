# 🎵 MP4 to MP3 Converter  

*A high-efficiency Python tool for seamless audio extraction from video files.*  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Dependencies](https://img.shields.io/badge/dependencies-moviepy-orange)  

## 🚀 Key Features  
- **Lossless Audio Extraction**: Preserves original audio quality during conversion.  
- **Lightweight & Fast**: Minimal dependencies, optimized for performance.  
- **CLI & Scriptable**: Designed for both standalone use and integration into pipelines.  
- **Robust Error Handling**: Validates inputs and provides clear feedback.  

## 📦 Installation  

### Prerequisites  
- Python 3.8+  
- FFmpeg (installed automatically via `moviepy`)  

```bash
pip install moviepy  # Install core dependency
```

## 🛠 Usage  

### Command Line  
```bash
python converter.py input.mp4 [-o output.mp3]  
```  

### As a Python Module  
```python
from converter import convert_mp4_to_mp3  
output_path = convert_mp4_to_mp3("video.mp4", "audio.mp3")  
```  

### Examples  
```bash
# Convert to default location (same directory)  
python converter.py lecture.mp4  

# Specify custom output path  
python converter.py demo.mp4 -o speech.mp3  
```  
## 📜 License

[LICENSE](LICENSE) © 2025 [IRUTABYOSE Yoramu](https://www.linkedin.com/in/iyoramu)

