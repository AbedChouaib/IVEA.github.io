# Random Burst Event - Advanced Settings

The Advanced Settings dialog provides additional configuration options for Random Burst Event analysis. These settings allow users to fine-tune event detection sensitivity, noise reduction, and fluorescence intensity tracking.

---

## Key Parameters and Descriptions

### Prominence (Default: Auto, User-Defined Option: p = 30)
- Defines the highest minimum value surrounding a local maximum.
- This parameter is automatically determined, but users can override it when the signal-to-noise ratio (SNR) is very low.

### Variation Time Window
- Defines the frame subtraction interval:
  - The algorithm subtracts frame (n+4) from frame (n) to detect intensity changes over time.

### Event Spread (See Paper for Details)
- Directly influences the Non-Maximum Suppression (NMS) algorithm, which helps filter overlapping detections and improves localization accuracy.

### Neural Network Confidence (Default: 0.5)
- Sets the probability threshold for neural network classification.
- Higher confidence values reduce false positives but may also cause some true events to be missed.

### Nomination Sensitivity (User-Defined Option)
- Adjusts the manual detection threshold sensitivity.
- Recommended for:
  - Low SNR videos
  - Videos with non-uniform fluorescence intensity (e.g., bright cell regions vs. faded cell regions).

### Gaussian Blur (Default: Enabled)
- Applies a Gaussian blur filter to reduce noise and smooth intensity fluctuations in the dataset.

### Adjust for Bleach Correction (Default: Enabled)
- Tracks fluorescence intensity variations over time to correct for photobleaching effects.

### Disable Log Info Prompt (Default: Disabled)
- Prevents IVEA from displaying informational messages in the ImageJ Log window.
