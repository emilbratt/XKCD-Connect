import json
import requests
# from settings import get_path
import os
import json

class database:

    def __init__(self):
        # path = os.path.dirname(os.path.realpath(__file__))
        os.makedirs('%s/Data'%os.path.dirname(os.path.realpath(__file__)), exist_ok=True)
        os.makedirs('%s/Images'%os.path.dirname(os.path.realpath(__file__)), exist_ok=True)


    def get_latest():
        # download newest json into a response object
        try:
            res_obj = requests.get('https://xkcd.com/info.0.json') # this url always contains json for latest comic
            res_obj.close()
        except requests.exceptions.ConnectionError:
            while True:
                print('Latest comic not found.')
                current = input('Type in a number manually:\n')
                if current.isdecimal() and int(current) > 0:
                    break

        # extract comic number from json object
        try:
            get_json = res_obj.json() # convert json to python dict
            current = get_json['num']

        # if extraction failed, type in a comic number manually
        except json.decoder.JSONDecodeError:
            while True:
                print('Latest comic not found.')
                current = input('Type in a number manually:\n')
                if current.isdecimal() and int(current) > 0:
                    break

        return current


    def get_database():
        # load comic database from json into python dict
        try:
            json_file = open('%s/Data/web_data.json'%os.path.dirname(os.path.realpath(__file__)),encoding='utf-8')
            comic_db = json.load(json_file)
            json_file.close()
        except FileNotFoundError:
            comic_db = {}
        except json.decoder.JSONDecodeError:
            comic_db = {}
        return comic_db


    def update_database(comic_db):
        json_file = open('%s/Data/web_data.json'%os.path.dirname(os.path.realpath(__file__)), 'w',encoding='utf-8')
        json.dump(comic_db, json_file, indent=2)
        json_file.close()


    def get_path():
        path = os.path.dirname(os.path.realpath(__file__))
        return path


    def list_images():
        stored_images = os.listdir('%s/Images'%os.path.dirname(os.path.realpath(__file__)))
        return stored_images
