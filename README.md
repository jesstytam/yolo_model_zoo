# YOLO model zoo
This is a (test) repo to run pre-trained YOLOv8 detection models. I recommend running the MegaDetector to remove non-animal images before running a finer-grained classification model, such as the ones here.

## Installation

Install Mamba Miniforge according to the instructions here[https://github.com/conda-forge/miniforge?tab=readme-ov-file#download]. This is essential for managing the packages required by this repository and their updates. Afterwards, you can follow the steps below to install and run `yolo_model_zoo`.

### Windows

```
mkdir c:\git
cd c:\git
git clone https://github.com/jesstytam/yolo_model_zoo
cd c:\git\yolo_model_zoo
mamba env create --file envs\environment.yml
mamba activate 
```

### MacOS & Linux

```
mkdir git
cd git
git clone https://github.com/jesstytam/yolo_model_zoo
cd yolo_model_zoo
mamba env create --file==environment.yml
mamba activate environment
```

## Run model

### Folder structure

### Models

### Training data

