# ROI Multi-Measurement Plugin

The **IVEA Multi-Measurement ROI Plugin** is designed to measure **fluorescence intensity profiles over time** within selected **Regions of Interest (ROIs)**.  
This plugin allows users to analyze **intensity fluctuations** in **single-channel or multi-channel** videos opened in ImageJ.  

It serves as a **helper plugin** for studying **IVEA-detected events** or analyzing **any ROI manually selected in ImageJ**.  

---

## Key Parameters and Options  

The plugin provides several **customizable options** for intensity measurement, available in the user interface.

### Frames Before (User-Defined Input, Default: 20)  
- Specifies the **number of frames before an event** to include in the measurement window.  

### Frames After (User-Defined Input, Default: 100)  
- Specifies the **number of frames after an event** to include in the measurement window.  

### All ROIs (Checkbox, Default: Unchecked)  
- If enabled, the plugin **measures intensity** across **all ROIs** in the **ROI Manager**.  

### All Opened Images (Checkbox, Default: Unchecked)  
- If enabled, the measurement is performed across **all opened video frames**.  

### Save Results (Checkbox, Default: Checked)  
- If enabled, the **measured intensity values** are saved to a **specified directory** for further analysis.  

### f - f₀ (Baseline Subtraction) (Checkbox, Default: Unchecked)  
- If enabled, **baseline subtraction** is applied using the equation:  
  \[
  f - f₀
  \]
  where:  
  - **f** = Current intensity  
  - **f₀** = Baseline intensity (pre-event intensity)  

### Normalize Range 0-1 (Checkbox, Default: Unchecked)  
- If enabled, **intensity values are normalized** between **0 and 1**, ensuring **uniform scaling** for comparative analysis.  

### Save Directory (Text Field & Browse Button)  
- Specifies the directory where **measurement results** will be saved.  
- Users can **manually enter a path** or use the **Browse button** to select a location.  

### Measure Button (Action Button)  
- **Initiates** the intensity measurement process based on the **selected parameters**.  

---