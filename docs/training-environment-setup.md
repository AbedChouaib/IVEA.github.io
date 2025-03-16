# Training Using IVEA Python - Environment Setup
```markdown
# IVEA

**Project Name**: IVEA  
**Python Version**: 3.8.10  
**TensorFlow Version**: 2.10.1 (with CUDA 11.2 / cuDNN 8.1.1 support)

This repository (folder named `IVEA_main`) contains all scripts for running the IVEA project. You’ll also find two text files:

1. **`requirements.txt`** – These are libraries required for the project **other than** TensorFlow.  
2. **`TensorFlow_Libs.txt`** – These are TensorFlow + dependencies specifically for TF 2.10.1.

---

## 🔧 Recommended Setup

For simplicity, we **highly recommend** using Anaconda.  
If you already have your own Python 3.8.10 environment, you can adapt the steps accordingly.

### 📂 1. Clone the Repository & Navigate

```bash
git clone https://github.com/AbedChouaib/IVEA.git
cd IVEA/IVEA_main
```

---

## 🛠️ Setting Up the Environment

### ✅ 2. Using Anaconda (Recommended)

```bash
conda create -n IVEA python=3.8.10
conda activate IVEA
```

### ✅ 3. Using a Virtual Environment (Alternative)

If you prefer using `venv` inside the `IVEA_main` directory instead of Conda:

```bash
python -m venv venv
```

Then, activate the virtual environment:

- **On Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **On Mac/Linux**:

  ```bash
  source venv/bin/activate
  ```

---

## 📦 Installing Dependencies

### 🛠️ 4. Install Basic Requirements (Before TensorFlow)

```bash
pip install -r requirements.txt
```

### 🛠️ 5. Install TensorFlow & Its Dependencies

```bash
pip install -r TensorFlow_Libs.txt
```

> **Note**: We do **not** use `tensorflow-gpu==2.9.1` here. Instead, `tensorflow==2.10.1` will work with GPU support when CUDA 11.2 and cuDNN 8.1.1 are installed.

---

## ⚡ (Optional) Installing NVIDIA Drivers for GPU Acceleration

For GPU support, ensure that:

1. Your **NVIDIA drivers** are up to date (supporting **CUDA 11.2**).
2. You have **CUDA 11.2** and **cuDNN 8.1.1** installed.

> If you’re on **Windows**, install the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) and then add cuDNN manually.  
> If you’re on **Linux**, follow your distro’s instructions or check the [NVIDIA documentation](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html).

If you don’t need GPU acceleration, you can **skip this step**.

---

## 🖥️ Setting Up Python Interpreter & VS Code

If you’re using **VS Code**, follow these steps:

1. **Open VS Code** and navigate to the `IVEA_main` folder:
   ```bash
   cd path/to/IVEA/IVEA_main
   code .
   ```

2. **Set up Python interpreter**:
   - Open the **Command Palette** (`Ctrl + Shift + P`).
   - Search for **"Python: Select Interpreter"** and click on it.
   - Choose:
     - `IVEA` (if using Conda)  
     - `.venv` (if using a virtual environment inside `IVEA_main`)

3. **Ensure VS Code recognizes your environment**:
   - If using `venv`, ensure the `Python: Default Interpreter Path` is set to:
     ```
     path/to/IVEA_main/venv/bin/python
     ```
   - If using Conda, it should be:
     ```
     path/to/anaconda/envs/IVEA/bin/python
     ```

Now, you’re ready to **run Python scripts inside VS Code!**

---

```bash
python IVEA_main.py
```
## ℹ️ Final Notes

✅ **Make sure you have the correct CUDA/cuDNN versions if you want GPU support.**  
✅ **Double-check pinned dependencies in `TensorFlow_Libs.txt` if you run into compatibility issues.**  
✅ **You can adjust versions in `requirements.txt`, but ensure compatibility with TensorFlow 2.10.1.**

Thanks for using **IVEA** – this guide should get you up and running quickly! 🚀
```
