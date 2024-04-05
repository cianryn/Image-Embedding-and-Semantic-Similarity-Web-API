import requests
from glob import glob
import argparse
import numpy as np
from tabulate import tabulate


parser = argparse.ArgumentParser("Semantic similarity analysis.")
parser.add_argument("--images_folder", default="images", help="path to all images")
parser.add_argument("--ref_image", default="cat.png", help="The reference image name")
args = parser.parse_args(args=[])

url = 'http://0.0.0.0:8080/upload-images/' # The URL of the FastAPI endpoint 
image_paths = glob(args.images_folder + "/*") # Paths to the image files 
files = [('files', (open(image_path, 'rb'))) for image_path in image_paths] # Prepare files in requests format
response = requests.post(url, files=files) # Send the POST request with the image files
for _, file_tuple in files:
    file_tuple.close() # Close files

# Extract FastAPI responses
response = response.json()
api_message = response["message"]
predictions = response["predictions"]
embeddings = response["embeddings"]


# Compute cosine similarity against reference image
def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

ref_embedding = embeddings[args.ref_image]
ref_embedding = np.array(ref_embedding)
similarities = {}
for key, embedding in embeddings.items():
    if key != args.ref_image:
        sim = cosine_similarity(ref_embedding, embedding)
        similarities[key] = sim
sorted_similarities = sorted(similarities.items(), key=lambda item: item[1])[::-1]


## Display top 10 similar results
print(api_message)
sorted_similarities = sorted_similarities[0:10]
headers = ["Reference Image", "Image Classification"]
table = [(args.ref_image, predictions[args.ref_image])]
print(tabulate(table, headers=headers, tablefmt="mixed_grid"))

headers = ["Images", "Similarity to Reference", "Image Classification"]
table = [(x[0],x[1],predictions[x[0]]) for x in sorted_similarities]
print(tabulate(table, headers=headers, tablefmt="mixed_grid"))






