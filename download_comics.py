import os
import requests

import json
from database_client import database
from visuals import loading_bar, up_lines

def download():

    path = database.get_path()

    comic_db = database.get_database()

    stored_images = database.list_images()

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
        image_file = open(image_path, "wb") # open byte object
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
