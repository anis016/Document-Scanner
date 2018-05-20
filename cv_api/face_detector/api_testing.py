# ur our face detection API to find faces in images via image url

import requests
import cv2
import os

# define the URL to our face detection API
web_url = "http://localhost:8000/face_detector/detect/"
WINDOW_NAME = "Face Detector"

def get_file_name(path):
    file_name = path.split("/")
    return file_name[len(file_name) - 1]

def make_folder():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    image_folder = os.path.join(dirname + "/", "saved_images")
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    return image_folder

def save_image(image_name):
    response = requests.get(payload["url"])

    image_folder = make_folder()
    image_path = os.path.join(image_folder + "/", image_name)

    with open(image_path, "wb") as image_file:
        image_file.write(response.content)

    return image_path

def call_api(payload):
    image_name = get_file_name(payload["url"])
    image_path = save_image(image_name)
    image = cv2.imread(image_path)

    response = requests.post(web_url, data=payload).json()
    print("{image_name}: {response}".format(image_name=image_name, response=response))

    # loop over the faces and draw them on the image
    for (startX, startY, endX, endY) in response["faces"]:
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # show the output image
    cv2.imshow(WINDOW_NAME, image)
    cv2.waitKey(0)

if __name__ == "__main__":
    payload = {"url": "https://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg"}
    call_api(payload)