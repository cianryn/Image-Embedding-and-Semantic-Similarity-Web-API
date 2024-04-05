import numpy as np
import torch
from torchvision.models import resnet18, ResNet18_Weights
import torchvision.transforms as transforms
from torch.autograd import Variable
from PIL import Image

## Initialization ##
im_path = "images/puppy.jpg"
embeddings = {}
model = resnet18(weights=ResNet18_Weights.DEFAULT)
model.eval()
layer = model._modules.get('avgpool')
scaler = transforms.Resize((224, 224))
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
to_tensor = transforms.ToTensor()

## Load images
image = Image.open(im_path)   
im = normalize(to_tensor(scaler(image))).unsqueeze(0) # Scale, to tensor, normalize + add batch dim


def hook_layer(module, inputs, output):
    print(output.detach().shape)
    embeddings[im_path] = output.data[0,:,0,0]

## Attach hook to avgpool layer
hook = layer.register_forward_hook(hook_layer)

# Perform a forward pass. The hook function will run automatically
with torch.no_grad():
    out = model(im)
hook.remove() # detach hook when done

