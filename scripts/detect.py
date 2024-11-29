import argparse
from ultralytics import YOLO
import torch
import os
import pandas as pd
import time

#setup argparse
parser = argparse.ArgumentParser(description='Run inference on a folder of images.')
parser.add_argument(
    '--model_name',
    default='best.pt',
    type=str,
    required=False,
    help='Path to the detector file.'
)
parser.add_argument(
    '--folder_path',
    default='data/input',
    type=str,
    required=False,
    help='Path to the folder of images.'
)
parser.add_argument(
    '--save_detections',
    default=False,
    type=bool,
    required=False,
    help='To save the detections with images or not.'
)
parser.add_argument(
    '--confidence',
    default=0.1,
    type=float,
    required=False,
    help='Confidence level of model.'
)
args = parser.parse_args()

#check cuda
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

#load model
model = YOLO(f'model_zoo/{args.model_name}').to(device)

#folder path to images
parent_dir = args.folder_path

#inference function
all_detections = []
def run_inference(parent_path):
    predictions = model.predict(source=parent_path,
                                save=args.save_detections,
                                save_txt=False,
                                save_conf=True,
                                imgsz=320,
                                conf=args.confidence,
                                iou=0.5)
    for result in predictions:
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            cat = int(box.cls[0])
            path = result.path
            class_name = model.names[cat]
            conf = float(box.conf[0])
            bbox = box.xywh.tolist()
            df = pd.DataFrame({'path': path,
                               'class_name': class_name,
                               'class_id': cat,
                               'confidence': conf,
                               'bbox': bbox})
            all_detections.append(df)

#run inference
for image in os.listdir(parent_dir):
    image_path = os.path.join(parent_dir, image)
    run_inference(parent_path=image_path)

#save detections to a single CSV file
timestamp = time.strftime("%Y%m%d_%H%M%S")
if all_detections:
    final_df = pd.concat(all_detections)
    final_df.to_csv(f'data/output/detections_{timestamp}.csv', index=False)
else:
    print("No detections were made.")
