# Stationary Event Tab - Advanced Settings

The **Advanced Settings** dialog provides additional configuration options for **Stationary Burst Event (SBE) analysis**.  
These parameters allow users to **fine-tune event detection, background noise filtering, and neural network sensitivity settings**.  

---

## Key Parameters and Descriptions  

### Erosion (Default: 0)  
- Applies an **erosion filter** to refine **detected regions** and minimize noise in the image.  

### Variation Time Window  
- Defines the **frame subtraction interval**:  
  - The algorithm **subtracts frame (n+4) from frame (n)** to detect changes over time.  

### Prominence (Default: Auto, User-Defined Option: p = 30)  
- Represents the **highest minimum value** surrounding a local maximum.  
- **Automatically detected**, but users can manually adjust it when the **signal-to-noise ratio (SNR) is very low**.  

### Add Frames (LSTM Model Only)  
- Extends the **analysis window time**, increasing the number of frames considered for event detection.  
- **Applicable only to LSTM-based models**.  
- Refer to the **associated research paper** for detailed methodology.  

### Neural Network Confidence (Default: 0.5)  
- Defines the **probability threshold** for neural network classification.  
- **Higher confidence values** reduce false positives but may also result in **missed true events**.  

### Nomination Sensitivity (User-Defined Option)  
- Adjusts the **detection threshold sensitivity** manually.  
- Useful when:  
  - The **signal-to-noise ratio (SNR) is low**.  
  - The video contains **non-uniform fluorescence intensity** (e.g., bright and dark regions within the same frame).  

### Gaussian Blur (Default: Enabled)  
- Applies a **Gaussian blur filter** to reduce **noise and smooth intensity variations** in the image.  

### Disable Log Info Prompt (Default: Disabled)  
- Disables IVEA’s **informational message prompts** in the ImageJ **Log window**.  

---