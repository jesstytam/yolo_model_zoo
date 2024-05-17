# YOLO model zoo

The purpose of this repository is to test pre-trained YOLOv8 models on a folder of images with minimal hyperparameter tuning. As such, feel free to modify `scripts/detect.py` and the folder structure to your liking, or add new models to the `model_zoo` folder when inferencing. Only YOLOv8 models are supported due to the slight changes in model architecture from YOLOv5. YOLOv9 models have not been tested yet.

In a real-world scenatio, please run the MegaDetector to remove all non-animal images before running a finer-grained detection and classification model, such as the ones here. YOLO models also work on video clips.

## Installation

Install Mamba Miniforge according to the instructions here[https://github.com/conda-forge/miniforge?tab=readme-ov-file#download]. This is essential for managing the packages required by this repository and their updates. Alternatively, you can also use your personal choice of package manager, e.g. Anaconda. Afterwards, you can follow the steps below to install and run `yolo_model_zoo`.

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

The default settings are as follows:
```
python scripts/detect.py
#OR
python scripts/detect.py --model_name yolov8s.pt --folder_path data/input --save_detections False --confidence 0.1
```

### Folder structure

Save your raw images are saved within `data/input` for the detection task. Detection results are saved in `data/output/detections.csv`

### Models

YOLOv8n is the smallest model size of only 6MB. It should be able to run on consumer-level GPUs.

### Training data

The dataset used for training the models here were part of the Ecoflow[https://github.com/microsoft/Ecoflow] dataset. From the 26 classes, I extracted 1000 random images from 14 of those classes for model training. The species included in the training dataset are as follows: <br />
  0: Brown Bandicoot <br />
  1: Red-necked Wallaby <br />
  2: Brushtail Possum <br />
  3: Cat <br />
  4: Red Fox <br />
  5: Rabbit Hare <br />
  6: Dog (or Dingo) <br />
  7: Eastern Grey Kangaroo <br />
  8: Echidna <br />
  9: Pig <br />
  10: Euro <br />
  11: Fallow Deer <br />
  12: Long-nosed Bandicoot <br />
  13: Koala <br />

## Contributing
If you have any suggestions, please create a new issue and I will respond when I have some free time.