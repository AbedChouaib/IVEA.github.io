# Random Burst Event  

This module is designed for analyzing mobile granules, including but not limited to T cells, chromaffin cells, INS1 cells, β cells, and other exocytotic systems. It facilitates event detection, classification, and measurement using neural network-based analysis techniques.

---

## Key Parameters and Features  

Each of the following settings is available as an input field or button within the GUI.

### Vision Radius  
- **Default: 14, Minimum: 6**  
- Defines the radius of the neural network visualization area (**patch size**) surrounding an event.  
- This parameter is crucial for event classification.  
- At each **ROI center**, IVEA extracts the surrounding area over a time interval, enabling the **Transformer neural network** to analyze this region effectively.  

### Search Radius  
- Determines the **ROI radius** surrounding an event.  
- Affects measurement accuracy and the **Non-Maximum Suppression (NMS) algorithm**.  

### Temporal Max Pooling  
- Reduces video frames using the **temporal max pooling** technique (**moving maximum intensity projection**).  
- Useful when:  
  - Event activity exceeds the neural network’s temporal vision limit (**26–28 frames**).  
  - Image acquisition frequency is particularly high (**e.g., 50 Hz**).  

### Measurement Window (a-b)  
- Defines the time interval for event measurement.  
- The **a-b** range represents the frame interval used for measurement calculations.  

---

## Model List  

Users can select from the following **pretrained models** for the **Random Burst Events** module:  

- **GranuVision3 (Default Model)**  
  - Encoder Vision Transformer trained on three exocytosis types:  
    - Fusion with a cloud  
    - Fusion without a cloud  
    - Latent vesicle fusion  

- **GranuVision2**  
  - Encoder Vision Transformer trained on two exocytosis types:  
    - Fusion with a cloud  
    - Fusion without a cloud  

- **GranuLSTM** (No longer supported)  
  - While outdated, users can still experiment with it as a **general classifier**.  

---

## Additional Detection Options  

### Detect Events Without Cloud (Category Label: 1)  
- Enables detection of **exocytosis events** that do not exhibit an observable cloud.  
- These events are classified as **abrupt disappearances**.  

### Detect Latent Vesicle Fusion (Category Label: 2)  
- Detects **exocytosis events** that occur suddenly **without prior vesicle presence**.  

### Include Small/Weak Events (Default: Enabled)  
- Allows detection of **low signal-to-noise ratio (SNR) events**.  

---

## Additional Features  

### Advanced Settings Button  
- Opens a **dialog window** for configuring default parameters for **non-fixed burst event (FBE) analysis**.  

### Custom Model Button  
- Opens a **dialog window** that allows users to:  
  - Export training data for **model customization**.  
  - Integrate **custom neural networks** into IVEA.  

---

