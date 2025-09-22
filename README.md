<h1 align="center">
  <br>
  <a href="https://github.com/KrishnashishMunshi/AnubisAV">
    <img src="https://github.com/hirakoisdead/AnubisAV/blob/main/assets/1x/logo.png" alt="AnubisAV" width="200">
  </a>
  <br>
  AnubisAV
  <br>
</h1>

<h4 align="center">
A lightweight and powerful open-source Anti-Virus software that performs **static malware analysis** on PE files using a machine learning model (LightGBM).
</h4>

<p align="center">
  <a href="https://github.com/KrishnashishMunshi/AnubisAV">
    <img src="https://img.shields.io/badge/version-1.0-blue.svg" alt="Version">
  </a>
  <a href="https://github.com/KrishnashishMunshi/AnubisAV/issues">
    <img src="https://img.shields.io/github/issues/KrishnashishMunshi/AnubisAV.svg" alt="Issues">
  </a>
  <a href="https://github.com/KrishnashishMunshi/AnubisAV/stargazers">
    <img src="https://img.shields.io/github/stars/KrishnashishMunshi/AnubisAV.svg" alt="Stars">
  </a>
</p>

<p align="center">
  <a href="#Key-Features">Key Features</a> •
  <a href="#Tech-Stack">Tech Stack</a> •
  <a href="#How-To-Use">How To Use</a> •
  <a href="#Project-Structure">Project Structure</a> •
  <a href="#Contributors">Contributors</a>
</p>

---

![AnubisAV Screenshot](https://github.com/hirakoisdead/AnubisAV/blob/main/assets/1x/preview.png)

---

## Key Features

- **ML-Powered Detection** – Uses LightGBM for static malware classification  
- **PE File Analysis** – Extracts key features from Windows executable files  
- **Cross-Platform** – Works on Windows, Linux, and macOS  
- **Simple Interface** – CLI & GUI support for ease of use  
- **Open-Source & Extensible** – Model and features can be updated easily  

---

## Tech Stack

- **Python 3.x** – Core language  
- **LightGBM** – Machine Learning model for malware detection  
- **PEfile** – PE header feature extraction  
- **Tkinter / Flask** – (if included) for GUI or web interface  

---

## How To Use

Clone this repository, set up dependencies, and run the main file.

```bash
# Clone this repository
git clone https://github.com/KrishnashishMunshi/AnubisAV.git
# Go into the project directory
cd AnubisAV

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Go into the GUI directory
cd gui

# Run the program
python3 page1.py
```
## Project Structure

```bash
AnubisAV/
├── assets/                # Logos, screenshots, icons
├── gui/                   # GUI or web interface code
├── thrember/              # Feature extraction / ML helper modules
├── EMBER2024_all.model    # Pretrained LightGBM model
├── classify.py            # Script to classify files
├── requirements.txt       # Python dependencies
```
## Contributors

Thanks to these amazing people for making **AnubisAV** possible!  

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/hirakoisdead">
        <img src="https://avatars.githubusercontent.com/hirakoisdead?v=4" width="80" style="border-radius:50%;" alt="Tanish"/>
        <br /><sub><b>Tanish</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/muaviz">
        <img src="https://avatars.githubusercontent.com/muaviz?v=4" width="80" style="border-radius:50%;" alt="Muaviz"/>
        <br /><sub><b>Muaviz</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Moon4546X">
        <img src="https://avatars.githubusercontent.com/Moon4546X?v=4" width="80" style="border-radius:50%;" alt="Achintya"/>
        <br /><sub><b>Achintya</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/KrishnashishMunshi">
        <img src="https://avatars.githubusercontent.com/KrishnashishMunshi?v=4" width="80" style="border-radius:50%;" alt="Krishnashish Munshi"/>
        <br /><sub><b>Krishnashish Munshi</b></sub>
      </a>
    </td>
  </tr>
</table>
