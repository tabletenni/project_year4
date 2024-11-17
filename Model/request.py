import requests

url = 'https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29'
file_name = 'yolov4-tiny.conv.29'

response = requests.get(url)

with open(file_name, 'wb') as f:
    f.write(response.content)

print(f"Downloaded {file_name}")