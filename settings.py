import os

def get_path():

    path = os.path.dirname(os.path.realpath(__file__))
    return path

def folder_Data(path):
    os.makedirs('%s/Data'%path, exist_ok=True)

def folder_Images(path):
    os.makedirs('%s/Images'%path, exist_ok=True)

def list_Images():
    stored_images = os.listdir('Images')
    return stored_images
