# Image Arranger Python Program 🖼️✨

Welcome to the **Image Arranger Python Program**! Using the powerful Pillow library, this program automatically sorts your images based on their dimensions, keeping them organized.

## 📂 What It Does

The program categorizes images into three folders based on their dimensions:

-   **Horizontal**: For images where the width is greater than the height. ➡️

-   **Vertical**: For images where the height is greater than the width. ⬆️

-   **Square**: For roughly square images (within a 10% tolerance). ⬜

## 🚀 How It Works

**Directory Structure:**

-  **The python program creates** the following directories if they don’t already exist:

    -   horizontal 🖥️
    
    -   vertical 📱
    
    -   square ⬜
 
 **Image Processing:**

-  **Scans** the ./src_img for image files with .jpg or .png extensions, opens each image, and determines its dimensions.

-  **File Movement**

-  Based on the image’s dimensions:

    -   Nearly square images move to the **square** folder.
    
    -   Images wider than tall move to the **horizontal** folder.
    
    -   Otherwise, images move to the **vertical** folder.

## 🛠️ Requirements

-   **Python 3.x** 🐍

-   **Pillow Library**

Clone this GitHub repository:

```bash
git clone https://github.com/LinuxSystemsEngineer/image_arranger.git
```

Change directories to the newly cloned GitHub repository:

```bash
cd image_arranger
```
Create a segmented Python virtual environment:

```bash
python3 -m venv .venv
```

Activate the segmented Python virtual environment:

```bash
source .venv/bin/activate
```

Install the required python library with the following:

```bash
pip3 install -r requirements.txt
```

## 💻 Usage

Place your image files (with .jpg or .png extensions) in the ./src_img directory as the script.

```bash
python3 image_arranger.py
```
---
Just let the script do all the work!

---
## 📝 License

### **MIT License**. ©️ 2025
