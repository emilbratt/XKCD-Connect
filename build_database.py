import requests
from visuals import loading_bar, up_lines
import json
from database_client import database

# fetch comic number, comic url, comic title and comic size from xkcd.com
def build_comic_db():

    print('Updating comic database...')

    current = database.get_latest()

    print(f'Latest comic number: {current}\n\n')

    comic_db = database.get_database()


    total = current - (len(comic_db.keys()))
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

                # store data from each variable into comic database
                comic_db[get_json['num']] = {
                'Title': get_json['safe_title'],
                'URL': get_json['img']
                }

            except UnboundLocalError:
                continue



            up_lines(1)
            print(f'Downloading comic data from https://xkcd.com/{get_json["num"]}'.ljust(80, ' '))
            iterate += 1
            loading_bar(iterate, total)

            if get_json["num"] % 10 == 0: # write to file every 10 iteration
                database.update_database(comic_db)


    database.update_database(comic_db)

    print('Building database done.\nThe databases was stored in: %s/Data/web_data.json'%database.get_path())

    return 0

if __name__ == '__main__':

    build_comic_db()
