# Hotspot Area Extraction - Advanced Settings

The **Advanced Settings** dialog provides additional configuration options for **Hotspot Area Extraction**.  
Each parameter is designed to improve **event detection accuracy** and **background noise filtering**.

---

## Key Parameters and Descriptions  

### Variation Time Window  
- Determines the **frame subtraction interval**:  
  - The algorithm subtracts **frame (n+3) from frame (n)** to detect variations over time.  

### Exclude Events in the Background  
- Prevents the **detection of events occurring in the background**.  

### Learn Background Noise (Disabled by Default)  
- Enables the software to **analyze and learn the background noise level**.  
- **Note:** If an event occurs in the background, this may **increase the sensitivity threshold**, potentially **bypassing weaker events**.  

### Frames to Learn From  
- Defines the **number of initial frames** used for **background noise detection**.  
- **Default: first 2 frames** (but can be adjusted for more frames as needed).  

### K-Means Clustering Algorithm  
- Allows users to set the **number of clusters (layers)** for **image segmentation**.  
- **If k = 1**, the **Multilayer Intensity Correction (MIC)** functions as a **simple ratio equation**.  
- Users can monitor the **segmentation results** in the **results folder** and adjust the **k value** accordingly.  

### Adaptive Threshold (Default: 0 - Off)  
- Enables **adaptive thresholding** to extract **the maximum number of detected regions**.  

### Global Threshold (Default: 0 - Auto)  
- Uses an **iterative thresholding method** for detecting event regions.  

### Override Global Threshold (Not Recommended)  
- Allows users to apply a **static threshold** instead of the **automatic iterative threshold**.  

---