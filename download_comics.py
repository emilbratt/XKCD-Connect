import os
import requests
from settings import list_Images, get_path
import json
from time import sleep
from settings import folder_Images, get_path
from visuals import loading_bar, up_lines

def download():
    # prepare path, folders and files
    path = get_path()
    folder_Images(path)

    json_file = open('%s/Data/web_data.json'%path,encoding="utf-8")
    comic_db = json.load(json_file)
    json_file.close()

    stored_images = list_Images()

    # extract URLs where we do not have stored the comic
    url_list = []
    for key in comic_db:
        if not os.path.basename(comic_db[key]['URL']) in stored_images:
            url_list.append(comic_db[key]['URL'])


    # download comics
    total = len(url_list)
    print(f'\nTotal comics do download: {total}')
    for iterate,url in enumerate(url_list):
        image_path = os.path.join("Images", os.path.basename(url))


        res = requests.get(url)
        res.raise_for_status()

        # open a binary object file
        image_file = open(image_path, "wb") #writes binary
        # ..and write binary data from object file (comic image) to image file
        for bytes in res.iter_content(100000):
            image_file.write(bytes)
        image_file.close()
        print((f'Downloading: {url}').ljust(90, ' '))
        print((f'Path: {image_path}').ljust(90, ' '))
        print(f'{total - iterate} images left')
        loading_bar(iterate, total)
        up_lines(3)


if __name__ == '__main__':
    download()
