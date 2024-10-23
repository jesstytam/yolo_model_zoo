# :paw_prints: YOLO model zoo :paw_prints:

The purpose of this repository is to test pre-trained YOLOv8 models on a folder of images with minimal hyperparameter tuning. As such, feel free to modify `scripts/detect.py` and the folder structure to your liking, or add new models to the `model_zoo` folder when inferencing. Only YOLOv8 models are supported due to the slight changes in model architecture from YOLOv5. YOLOv9 models have not been tested yet.

In a real-world scenatio, please run the MegaDetector to remove all non-animal images before running a finer-grained detection and classification model, such as the ones here. YOLO models also work on video clips.

## :axe: Installation

Install Git [here](https://www.git-scm.com/downloads) and Mamba Miniforge according to the instructions [here](https://github.com/conda-forge/miniforge?tab=readme-ov-file#download), and then open `Miniforge Prompt`. This is essential for managing the packages required by this repository and their updates. Alternatively, you can also use your personal choice of package manager, e.g. Anaconda. Afterwards, you can follow the steps below to install and run `yolo_model_zoo`. When running the following code, be sure to run them one line after another instead all together, in order to catch errors easier.

### Windows

Navigate to a folder where you would like to have this repository saved and download it:
```
mkdir c:\git
cd c:\git
git clone https://github.com/jesstytam/yolo_model_zoo
```
Navigate into the repository's folder to create an environnent and install the YOLO package:
```
cd yolo_model_zoo
mkdir data\output
mamba create -n yolov8 python=3.10
mamba activate  yolov8
pip install ultralytics
```

### MacOS & Linux

Navigate to a folder where you would like to have this repository saved and download it:
```
mkdir git
cd git
git clone https://github.com/jesstytam/yolo_model_zoo
```
Navigate into the repository's folder to create an environnent and install the YOLO package:
```
cd yolo_model_zoo
mkdir data/output #creates a folder to store your results
mamba create -n yolov8 python=3.10 #creates environment to store your packages
mamba activate yolov8
pip install ultralytics
```

## :fondue: Run model

The default settings are as follows:
```
python scripts/detect.py
#OR (these 2 lines are the same)
python scripts/detect.py --model_name yolov8s.pt --folder_path data/input --save_detections False --confidence 0.1
```

### Folder structure

Save your raw images are saved within `data/input` for the detection task. Detection results are saved in `data/output/detections.csv`

### Models

YOLOv8n is the smallest model size of only 6MB. It should be able to run on consumer-level GPUs.

### Training data

The dataset used for training the models here were part of the [Ecoflow](https://github.com/microsoft/Ecoflow) dataset. From the 26 classes, I extracted 1000 random images from 14 of those classes for model training. The species included in the training dataset are as follows: <br />

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

## :climbing_man: Contributing
If you have any suggestions, please create a new issue and I will respond when I have some free time.
