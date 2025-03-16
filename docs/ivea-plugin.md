# IVEA Plugin

![Logo](https://github.com/AbedChouaib/IVEA/blob/main/resources/IVEA%20logo%20x256.png)  

**Author:** Eng. Abed Chouaib  
**Supervisors:** Dr. Ute Becherer (University of Saarland, CIPMM) | Dr. Ali Shaib (University Medical Center Göttingen)  

## 📖 About  

**IVEA (Intelligent Vesicle Exocytosis Analysis Platform)** is an open-source **Fiji/ImageJ** plugin that utilizes artificial intelligence to detect and analyze exocytosis events in a variety of cell types.  
IVEA is designed to provide fully automated, high-speed batch analysis using state-of-the-art deep learning models.  

### 🔬 **AI-Powered Exocytosis Detection**  
IVEA integrates advanced **Vision Transformer (ViT)** and **LSTM (Long Short-Term Memory)** neural networks, enabling robust detection of random burst exocytosis events and stationary burst events in neurons.  

🔹 **Publication:** [Read the Paper](https://www.biorxiv.org/content/10.1101/2024.08.02.606323v1)  

---

## Table of Contents  

- [Installation](#installation)  
- [Features](#features)  

---

# 🛠️ Installation  

1️⃣ **Download the latest IVEA plugin:**  
   - [Latest Release](https://github.com/AbedChouaib/IVEA/releases/tag/IVEA_v2.0)  
   - [Version 2 (Paper Results)](https://github.com/AbedChouaib/IVEA/releases/tag/IVEA_v2.0)  

2️⃣ **Get the source code:**  
   - [Source Code](https://cloud.hiz-saarland.de/s/eEaF4A8eWpr88Qf)  

3️⃣ **Download Fiji/ImageJ:**  
   - [ImageJ Fiji](https://imagej.net/software/fiji/)  

4️⃣ **Download test data:**  
   - [Test Data](https://cloud.hiz-saarland.de/s/zwipttdc6ySCLzC)  

5️⃣ **Install the plugin:**  
   - **Option 1:** Drag and drop the **IVEA .jar** file into ImageJ.  
   - **Option 2:** Copy and paste the **IVEA .jar** file into the **ImageJ plugin directory**, then restart ImageJ.  

---

# Features  

✅ **AI-Powered Detection**  
- Employs Vision Transformer (ViT) and LSTM networks to detect exocytosis events across various cell types.  

✅ **Fully Automated Batch Analysis**  
- No manual intervention required—simply load your data, and IVEA will process it automatically.  

✅ **User-Friendly GUI**  
- Intuitive and easy-to-use graphical interface for streamlined analysis.  

✅ **Pretrained Models Included**  
- Multiple pretrained deep learning models available within IVEA.  

✅ **Custom Model Training Support**  
- Users can train and integrate custom models into the IVEA pipeline.  

✅ **Supports Any Image Stack**  
- Compatible with image stacks of any resolution and length.  

✅ **High-Speed Processing**  
- Optimized for efficiency, processing videos in seconds (e.g., **256x256, 3000 frames**).  

---

# 📂 Plugin Location in ImageJ  

Once installed, IVEA will appear in ImageJ's plugin menu:  

📂 **Menu Path:** `Plugins > IVEA`  

IVEA provides multiple analysis modules, each designed for a specific purpose:  

### **Analysis Modules**  

| Module | Functionality |
|--------|--------------|
| **Random Burst Event** | Detects non-stationary, spontaneous exocytosis events using deep learning models. |
| **Stationary Burst Event (Neurons)** | Identifies exocytosis events localized to specific regions in neurons. |
| **Hotspot Area Detection** | Uses K-means clustering and global iterative thresholding to identify active regions. |
| **ROI Multi-Measurement** | Extracts intensity profiles over a time interval for specified **Regions of Interest (ROIs)**. |
| **Data Labeling** | Provides an annotation tool for training datasets used in IVEA's deep learning models. |

---

# 📂 IVEA Resources  

Upon installation, IVEA automatically creates a directory named "IVEA Resources" inside the ImageJ Plugins directory.  

### 📂 Contents of the `IVEA Resources` Folder  
- **Pretrained Deep Learning Models**  
- **IVEA Software Configuration File**  

This folder is essential for storing and managing model weights, ensuring the correct functioning of IVEA’s AI-based detection system.  

---

# ℹ️ Notes  

- **IVEA is continuously evolving**, with planned improvements for deep learning models, and advanced data analysis tools.  
- For updates and community discussions, visit the **[GitHub Repository](https://github.com/AbedChouaib/IVEA)**.  

**We welcome feedback to enhance IVEA’s capabilities!**  

