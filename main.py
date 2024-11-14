import os
import shutil
import zipfile
import subprocess
import requests
import urllib.request

# พาธต้นทางของไฟล์ zip
source_path = 'obj.zip'


# คัดลอกไฟล์ไปยังโฟลเดอร์ darknet
destination_path = 'darknet/data/obj.zip'
shutil.copy(source_path, destination_path)

with zipfile.ZipFile(destination_path, 'r') as zip_ref:
    zip_ref.extractall('darknet/data/')

print("Datasets have been copied and unzipped successfully.")
script_path = os.path.join(os.getcwd(), 'darknet', 'data', 'process.py')
subprocess.run(['python', script_path])

data_folder = '/darknet/data'
if os.path.exists(data_folder):
    print("Files in 'data/' folder:")
    for file_name in os.listdir(data_folder):
        print(file_name)
else:
    print(f"Folder '{data_folder}' does not exist.")


url = 'https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29'
file_name = 'yolov4-tiny.conv.29'

urllib.request.urlretrieve(url, file_name)

print(f"Downloaded {file_name}")