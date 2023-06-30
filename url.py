import zipfile
import os
import requests

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def download_and_extract_zip(url, extract_path, zip_filename):
    create_folder_if_not_exists(extract_path)
    response = requests.get(url)
    response.raise_for_status()

    with open(zip_filename, "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(zip_filename, "r") as zip_ref:
        zip_ref.extractall(extract_path)
        print(f'Repository was saved in {extract_path}/{zip_filename[:-4]}')

    os.remove(zip_filename)