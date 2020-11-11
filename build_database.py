import requests
from visuals import loading_bar, up_lines
import json
import os
# scrape xkcd and store comic number, comic url, comic title and comic size into dictionary
def build_comic_db():
    # prepare path, folders and files

    os.makedirs('Data', exist_ok=True)
    cwd = os.path.dirname(os.path.realpath(__file__))
    # print(path)
    exit()



    print('Building comic database...')

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

    print(f'Latest comic number: {current}\n')

    # load comic database from json into python dict
    try:
        json_file = open('data.json',encoding="utf-8")
        comic_db = json.load(json_file)
        json_file.close()
    except FileNotFoundError:
        comic_db = {}
    except json.decoder.JSONDecodeError:
        comic_db = {}



    length = current - (len(comic_db.keys()))
    iterate = 0
    # build comic database
    for comic in range(1, int(current)+1):

        # skip every comic that is already in database
        if str(comic) in comic_db:
            continue
        else: # if not in comic database, fetch data from web
            try:
                res_obj = requests.get(f'https://xkcd.com/{str(comic)}/info.0.json')
                res_obj.close()
            except requests.exceptions.ConnectionError:
                print(f'Skipping comic number {str(comic)}\n')
                sleep(2)
                continue
            try:
                get_json = res_obj.json() # convert json to python dict
            # so lets ignore this one
            except json.decoder.JSONDecodeError:
                if comic != 404: # xkcd jokingly left out comic with number 404
                    print(f'Error fetching json from response object from \
https://xkcd.com/{str(comic)}/info.0.json.\nskipping this comic..\n')
                    sleep(2)
                    continue
            try:
                # create variables for each value
                # size
                response_object_image = requests.get(get_json['img'], stream=True)
                res_obj.close()
                comic_size = response_object_image.headers.get('content-length')
                # comic title
                comic_title = get_json["safe_title"]
                # comic id
                comic_number = get_json['num']
                # direct URL to comic image
                comic_URL = get_json['img']

                # store data from each variable into comic database
                comic_db[comic_number] = {
                'Title': comic_title,
                'URL': comic_URL,
                'Size': comic_size
                }
            except requests.exceptions.ConnectionError:
                print('Error fetching image url, skipping this comic..\n')
                continue
            except UnboundLocalError:
                continue


            print(f'Downloading comic data from https://xkcd.com/{comic_number}')
            iterate += 1

            loading_bar(iterate, length)
            if comic_number % 10 == 0:
                json_file = open('data.json', 'w',encoding="utf-8")
                json.dump(comic_db, json_file)
                json_file.close()


if __name__ == '__main__':

    build_comic_db()
