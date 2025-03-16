# Training Using IVEA Python - Main Script GUI

The **IVEA_main** script serves as the **central interface** for running the **IVEA Python GUI**.  
This section provides **detailed instructions** on how to **train a new model, create datasets, and refine existing models** within IVEA.  

---

## Main Script GUI  

### 1️⃣ Training a New Model  

To train a new model using IVEA, follow these steps:  

#### **Step 1: Import Your Dataset**  
- Open the **IVEA_main** script.  
- Locate the **Your Current Dataset** field.  
- Import the dataset by **specifying the path** to your **HDF5 (.h5) file**.  

#### **Step 2: Select the Training Option**  
- In the **Select Model** dropdown menu, choose **Train new model**.  

#### **Step 3: Initiate Training**  
- Click on the **Train Model** button to **start training**.  

---

### 2️⃣ Creating a New Dataset  

If you do **not** have an existing dataset, you can **generate one** from your **labeled video files**.  

#### **Step 1: Specify the Video Directory**  
- Locate the **Videos Directory (TIFF)** field.  
- Import the directory containing your **TIFF video files**.  

#### **Step 2: Generate the Dataset**  
- Click on the **Create Dataset** button.  
- The system will **automatically process** the videos and generate an **HDF5 dataset**.  
- Once completed, the **new dataset location is loaded automatically**.  

#### **Step 3: Train the Model**  
- Click on the **Train Model** button to **start training** using the **newly created dataset**.  

---

### 3️⃣ Combining Datasets  

To **merge new data** with an **existing dataset**, follow these steps:  

#### **Step 1: Import Data Sources**  
- Import the **directory containing the new video files**.  
- Import the **directory of your current dataset**.  

#### **Step 2: Combine the Datasets**  
- Click on the **Combine Dataset** button.  
- The datasets will be **merged** into a **larger dataset**.  
- The software will **automatically update its reference** to the new dataset.  

#### **Step 3: Start Training**  
- Click on **Train Model** to **train** using the **newly combined dataset**.  

---

### 4️⃣ Refining an Existing Model  

IVEA supports **model refinement** using your **custom dataset**.  
Currently, two models are available for refinement:  

- **GranuVision3**  
- **NeuroVision1**  

#### **Step 1: Select the Model to Refine**  
- In the **Select Model** dropdown menu, choose the model you wish to refine.  

#### **Step 2: Provide Training Data**  
- Import the **directory containing your labeled video files** (ROI files, ZIP, or ImageJ ROI files).  

#### **Step 3: Prepare the Dataset**  
- Click on the **Create Dataset** button to **process the videos** and generate a new dataset.  
- If you **already have a saved dataset**, simply **specify its directory path**.  
- Once imported, the software **remembers your last working directory** for future sessions.  

#### **Step 4: Train the Model**  
- Click on **Train Model** to refine the **selected model**.  

---

### 5️⃣ Managing Output Files  

All **output files**, including **trained models and datasets**, are stored in the **project directory** under **IVEA_main**.  

#### **Customizing the Output Directory**  
- Modify the **JSON configuration files** in the **settings directory**.  
- There are **three JSON files**, each corresponding to a **specific model** available in the **Select Model list**.  

---