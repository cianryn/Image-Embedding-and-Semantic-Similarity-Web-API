
from fastapi import FastAPI, File, UploadFile
from typing import List
from PIL import Image
import io
import numpy as np
import torch
from torchvision.models import resnet18, ResNet18_Weights
import torchvision.transforms as transforms
from torch.autograd import Variable
from fastapi.responses import JSONResponse

app = FastAPI()

## Initialization for Embedding Model
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)
model.eval()
layer = model._modules.get('avgpool')
scaler = transforms.Resize((224, 224))
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
to_tensor = transforms.ToTensor()

@app.post("/upload-images/")
async def create_upload_files(files: List[UploadFile] = File(...)):

    embeddings = {}
    predictions = {}

    for file in files:
        
        # if file.content_type not in ["image/jpeg", "image/png"]:
        #     return JSONResponse(status_code=400, content={"message": f"Invalid file type: {file.filename}"})

        try:
            image_bytes = await file.read() 
            image_bytes = io.BytesIO(image_bytes)
            im = Image.open(image_bytes).convert('RGB')
            im = normalize(to_tensor(scaler(im))).unsqueeze(0) # Scale, to tensor, normalize + add batch dim
            def hook_layer(module, inputs, output):
                embeddings[file.filename] = output.data[0,:,0,0].detach().tolist()
            hook = layer.register_forward_hook(hook_layer) ## Attach hook to avgpool layer
            with torch.no_grad():
                out = model(im) # Perform a forward pass. The hook function will run automatically
                class_id = out.argmax().item()
                category_name = weights.meta["categories"][class_id]
                predictions[file.filename] = category_name
            hook.remove() # detach hook when done

        except Exception as e:
            return JSONResponse(status_code=500, content={"message": f"Error processing {file.filename}: {str(e)}"})

    # return JSONResponse(content={"embeddings": embeddings})
    return {"message": "You uploaded {} image(s)".format(len(files)), 
            "predictions": predictions,
            "embeddings": embeddings
            }