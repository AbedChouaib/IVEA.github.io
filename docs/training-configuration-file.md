# Training Using IVEA Python - Configuration File
```markdown
## ▶️ IVEA config files parameters adjustment


📂 **Configuration Files:**  
- Located in the **`settings`** directory.
- The main configuration files are:
  - **`default.json`** – Used for general training settings.
  - **`GranuConfig.json`** – For granular model configurations.
  - **`NeuroConfig.json`** – For neural model configurations.

⚙️ **How Configuration Selection Works:**  
- **Model Selection**: Choosing a specific model type will automatically apply the corresponding configuration file.  
- **New Training Session**: If starting a fresh training session, the system will default to using `default.json`.  

Make sure to adjust the configuration files as needed to match your training requirements.
```

```markdown
# 📄 Configuration File Parameters for IVEA  

This document explains the parameters within the configuration file for the IVEA software. If any parameter requires additional details, they are marked accordingly.

---

## **Class Mapping (`classes_map`)**  

The **`classes_map`** section defines the classification labels and their respective properties. Each entry includes:  

- **`class_label`**: A list of numerical labels assigned to this class. A class may have multiple labels, allowing flexibility in data labeling.  
  - Example: A feature labeled as **`1`** and **`11`** might represent similar but slightly different structures. If the neural network struggles to distinguish them, we can initially assign separate class IDs (e.g., `1` → `ID 1`, `11` → `ID 3` for fusion cases). If the network successfully differentiates them, they may share the same ID (`1`).  
- **`class_id`**: A unique identifier for the class.  
  - Positive **IDs** correspond to standard classifications.  
  - Negative **IDs** represent fusion events, ensuring they are correctly processed and stacked accordingly.  
- **`radius`**: Defines the spatial extent of the class (i.e., the **vesicle/fusion size** as seen by the network).  
  - If set to `null`, the **default radius** (see `default_radius`) is applied.  
  - If specified, it overrides the default radius for this class.  

📌 **Adding a New Class**:  
To add a new class, simply copy an existing entry within `classes_map`, modify the `class_label`, assign a unique `class_id`, and define an appropriate `radius`.  

```json
{"class_label": [9], "class_id": 9, "radius": 13}
```
- This adds a new class labeled `9` with ID `9` and a radius of `13`.  

---

## 📂 **File & Dataset Parameters**  

| Parameter           | Description |
|---------------------|-------------|
| **`class_tag`**     | Tag used for class annotation within datasets. |
| **`roi_file_tag`**  | Tag used for labeling **Region of Interest (ROI)** files used in training. |
| **`file_extension`** | Defines the format of the input files (default: `"tif"`). |
| **`outfile_dataset_name`** | Name of the output dataset file. |
| **`model_name`** | Name of the neural network model used (e.g., `"GranuCalciumVision3"`). |
| **`model_type`** | Defines the type of model (e.g., `"random", "stationary"`). |
| **`timeseries`** | Number of frames analyzed per input sequence (default: `26`). |
| **`more_frames`** | Number of additional frames added **after** the event for analysis. |
| **`default_radius`** | The fallback radius used when `radius` is set to `null` in `classes_map`. |
| **`class_nolabel`** | If a class is **not labeled**, it is assigned a default label (`3`). Set this to `null` to disable automatic labeling of unlabeled regions. |
| **`radius_nolabel`** | Default radius used for unlabeled classes. |

📌 **Time-Series Breakdown**  
- **`timeseries = 26`** → The vision transformer model processes `13` frames **before** and `13` frames **after** the event.  
- **`more_frames = 2`** → Adds **two additional frames after the event**, increasing the total processed frames to **28** per patch.  

---

## 🔧 **Data Handling Parameters**  

| Parameter         | Description |
|-------------------|-------------|
| **`num_augmentation`** | Number of augmentation operations applied to the dataset. |
| **`augment_data`** | Enables (`true`) or disables (`false`) data augmentation. |
| **`save_data`** | Enables (`true`) or disables (`false`) saving the processed dataset. |
| **`output_dir`** | Directory where output data is saved. |
| **`dataset_path`** | Path to an existing dataset file. |

📌 **Using an Existing Dataset for Training**  
- If training a new model using an **existing dataset**, provide the `.h5` dataset file in the `dataset_path`.  
  Example:  
  ```
  D:/project/CTL-CC-INS_dataset_c11r14_sc16_f3_t26_m2_cd63.h5
  ```

---

##  **Neural Network Parameters**  

| Parameter        | Description |
|-----------------|-------------|
| **`epoch_num`**  | Number of training epochs. |
| **`batch_size`** | Number of samples processed per training batch. |
| **`dropout_rate`** | Dropout rate used to prevent overfitting (`0` = no dropout). |
| **`call_patience`** | Number of epochs without improvement before early stopping is triggered. |
| **`learning_rate`** | The learning rate for the optimizer (`3e-4` by default). |
| **`scale_radius_to`** | Rescales all radii to a fixed value (`16`). **Please clarify its exact usage in the network.** |

---

## ℹ️ **Additional Notes**  

- **Comments and notes**: The config file has comments and notes that have no purpose other than to be informative.

**For any custom modifications, ensure that `classes_map` is correctly structured to reflect your data labeling strategy.**  
```