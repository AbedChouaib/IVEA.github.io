# Labeling New Data  

The **IVEA Data Labeling Plugin** is designed for labeling new data intended for training or refining models.  
This plugin enables users to efficiently categorize **events** and **artifacts** to enhance the performance of IVEA’s machine learning models.

---

## Labeling Categories  

### Exocytosis Labels (Positive Integers)  

The following labels are assigned to **exocytosis events**:  

- `0` – Fusion with a cloud  
- `1` – Fusion without a cloud  
- `2` – Latent vesicle fusion  

### Noise and Artifact Categories (Negative Integers)  

Negative integer values are used to classify **noise and artifacts**:  

- `-1` – Random noise  
- `-2` – Vesicle intensity fluctuation  
- `-3` – Moving vesicle  
- `-4` – Random noise with intensity fluctuations  
- `-5` – Intensity flickering and out-of-focus artifact  
- `-6` – Intensity rise (vesicle docking)  
- `-7` – Intensity decrease (vesicle undocking)  
- `-8` – Light movement (e.g., passing light, cloud spreading as a wave, etc.)  

---

## Customizing Labels  

The available labels are directly controlled by the IVEA JSON configuration file, included with the Python training project.  

Users have the ability to:  

- Modify existing labels to refine classification criteria.  
- Add new label categories to expand the dataset's classification capabilities.  
- Adjust dataset labeling for new datasets or modify existing datasets to fit specific research needs.  

Expert users can further customize and optimize **labeling parameters** to improve model training and performance.

---



