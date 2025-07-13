import requests
import os

# GitHub API URL to list contents of a folder
api_url = "https://api.github.com/repos/Neural-Network-Research-Paper/Image-Batches/contents/batch1" #You are to change the batch1 to batch2, batch3 and so on the numbers assigned to you 
# Create a local folder
response = requests.get(api_url)
files = response.json()

for file in files:
    if file['name'].endswith(('.jpg', '.png', '.jpeg')):
        download_url = file['download_url']
        filename = file['name']
        print(f"Downloading {filename} from {download_url}...")
        img_data = requests.get(download_url).content
        with open(os.path.join("image_folder", filename), 'wb') as f:
            f.write(img_data)

print("✅ All images downloaded successfully.")
