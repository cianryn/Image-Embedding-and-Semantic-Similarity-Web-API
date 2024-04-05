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

## Applications

1. Image Search Engines
    * By comparing embeddings, search engines can find images similar to a query image. This is useful in reverse image search applications where the goal is to find images that are visually similar to a given image.
2. Content-Based Image Retrieval (CBIR)
    * CBIR systems use image embeddings to enable searching and retrieving images from large databases based on content similarity rather than metadata or tags. This is widely used in digital libraries, stock photo databases, and e-commerce for product search.
3. Recommendation Systems
    * E-commerce and social media platforms use image similarity to recommend visually similar products or content to users. For example, fashion retailers suggest items similar to what a user is viewing, enhancing user engagement and potential sales.
4. Duplicate Detection
    * Image similarity can identify duplicate or near-duplicate images within a dataset, helping clean up databases by removing redundant information. This is crucial for maintaining the efficiency and accuracy of image-based systems.
5. Face Recognition and Verification
    * By extracting and comparing facial features, systems can recognize individuals across different images. This technology underpins security systems, personalized experiences in tech products, and tools for organizing photos based on who is in them.
6. Medical Image Analysis
    * In healthcare, CNN embeddings can help compare and analyze medical images, such as X-rays or MRI scans, to identify patterns, anomalies, or disease markers by referencing similar cases from a medical image database.

## Possible Improvements 
- [ ] Mercury
- [x] Include network classification predicitons to better understand similarity measurements
- [ ] Explore other similarity metrics
- [ ] Explore alternative CNN's for improved embeddings
- [ ] Create Vector database for already seen images to improve efficiency














