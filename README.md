# Semantic Similarity Web API with Image Embeddings
Web API and a client application that leverages pre-trained CNN's to generate image embeddings for semantic similarity analysis. </br>
The project is split into 2 components: </br>
1. FastAPI that takes multiple images and provide image embeddings and image classification predictinos. </br>
2. Command line client script that computes the similarity between a reference images ans a list of images



## Installation

### FastAPI Web Service
To create docker image and run docer container, run the following command lines: </br> 
`docker build -t fastapi-image-embeddings .` (may take a few mintes) </br>
`docker run -p 8080:8080 fastapi-image-embeddings` (port 8080 is exposed) </br> 

### Image Similarity Analysis
To compute similarity against reference image, run the following command: </br> 
`pip install -r requirements.txt` </br> 
`python similarity_analysis.py` </br> 

Default parameters will be selected for analysis using test images in */images*. </br> 
Optional parameters include: </br> 
* images_folder : The path to the folder containing all images including reference image `default = images` </br>
* ref_image : The refence image name from which we compare the other images to. `default = cat.png` </br> 
</br> **Example**: python similarity_analysis.py --images_folder images --ref_image cat.png

## Example Output

## Possible Improvements
- [x] Include network classification predicitons to better understand similarity measurements
- [] Explore other similarity metrics
- [] Explore alternative CNN's for improved embeddings
- [] Create Vector database for already seen images to improve efficiency














