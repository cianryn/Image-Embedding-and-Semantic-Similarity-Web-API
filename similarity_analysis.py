import requests
from glob import glob


url = 'http://0.0.0.0:8080/upload-images/' # The URL of the FastAPI endpoint 
image_paths = glob("images/*") # Paths to the image files 
files = [('files', (open(image_path, 'rb'))) for image_path in image_paths] # Prepare files `requests` format
response = requests.post(url, files=files) # Send the POST request with the image files

# Close files
for _, file_tuple in files:
    file_tuple.close()

# Print the response from the server
print(response.json()["predictions"])
for key, embedding in response.json()["embeddings"].items():
    print(key, len(embedding))
