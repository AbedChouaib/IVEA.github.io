# Stationary Event Module

The **Stationary Event Module** is designed for the analysis of videos where **stationary events occur at neuronal synapses**, such as **Dorsal Root Ganglion (DRG) neurons**.  
This module provides **precise event detection and processing** for **stationary burst events** in neuronal imaging.  

---

## Key Parameters and Features  

Each of the following settings is available as an **input field** or **button** within the **GUI**.

### ROI Radius  
- Defines the **size of the Region of Interest (ROI)** surrounding an event.  
- Directly influences the **accuracy of event measurements**.  

### Temporal Max Pooling  
- Applies a **temporal max pooling technique** (moving maximum intensity projection) to reduce the number of video frames.  
- Useful in cases where:  
  - Event activity **slows down and exceeds the neural network’s temporal vision limit (40 frames)**.  
  - The **image acquisition frequency** is high (**e.g., 50 Hz**).  

---

## Model List  

Users can select from the following **pretrained models** for **stationary burst event** analysis:  

- **NeuroLSTM** (Default Model)  
  - An **LSTM-based model** specialized for **synaptic neuron exocytosis events**.  

- **NeuroVision1**  
  - An **encoder-based Vision Transformer** model trained on three synaptic neuron exocytosis types:  
    - Short exocytosis  
    - Long-stay exocytosis  
    - Slow exocytosis  

- **GranuVision3**  
  - Another **encoder-based Vision Transformer** model, trained on **granules**.  
  - Similar to the model used in the **Random Burst Events** module.  

**Important:**  
- The **Vision Transformer models in this module are experimental**.  
- They have been tested on a **limited dataset**, and **performance may vary**.  
- These models are **under continuous development and improvement**.  

---

## Stimulation Detection  

### Stimulation Detection Feature  
- Designed to detect **strong stimulation events**, such as those occurring in **DRG neurons**.  

### Stimulation (a-b)  
- Defines the **stimulation timing window**:  
  - **a-b** represents the time range of stimulation.  
  - If **a** or **b** is set to `0`, the values are **determined automatically**.  
  - Use **"_"** to indicate **multiple stimulation events**.  

---

## Additional Features  

### Advanced Settings Button  
- Opens a **dialog window** for configuring **Fixed Burst Event (FBE) analysis** parameters.  

### Measurements Button  
- Opens a **dialog window** allowing users to **customize measurement settings** for event analysis.  

---