import torch

# Model
model = torch.hub.load('model_zoo/test.pt', pretrained=True)

# Images
imgs = ['data/input']  # batch of images

# Inference
results = model(imgs)