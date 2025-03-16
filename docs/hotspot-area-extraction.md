# Hotspot Area Extraction Module

The **Hotspot Area Extraction** module is designed for analyzing **videos with fixed image acquisitions**, such as **AndromeDA nanosensor paint experiments**.  
This module enables **precise event detection and hotspot localization** by applying advanced **filtering, selection, and brightness correction techniques**.  

---

## Key Parameters and Controls  

Each of the following settings is available as either an **input parameter field** or a **button** within the **GUI**.

### Noise Filter Radius  
- Uses a **median filter** to eliminate **noise** before applying the **iterative global threshold**.  
- **Default: 8 pixels**.  

### Selection Enlargement  
- Expands the **Region of Interest (ROI)** by **n pixels** to include **surrounding areas**.  

### Event Center Search Radius  
- Defines the **spatial tracking radius** for identifying the **center of detected events**.  

### Brightness Adjustment  
- Controls **fluorescence intensity fluctuations** using the **Multilayer Intensity Correction (MIC) algorithm**.  
- Set this value to **0** if **no intensity fluctuations** are present in the dataset.  

### Create Mask Button  
- Allows users to **manually select a region** within the video(s) for **noise identification**.  
- **Important:** Do **not** select areas where **events may occur**, as this may **affect detection accuracy**.  

### Advanced Settings Button  
- Opens a **dialog window** containing **default parameters** for **Hotspot Area Extraction**.  

---