import random
from database_client import database
import webbrowser
from time import sleep
def open_random_comic():

    comic_db = database.get_database()
    fail_safe = 10
    while True:

        if fail_safe == 0:
            print('\n\n\t\tCant load comic from xkcd.com..\n')
            sleep(2)
            break
        try:
            webbrowser.open(comic_db[str(random.randint(1,len(comic_db)))]['URL'])
            # webbrowser.open(comic_db[str(0)]['URL'])
            break
        except KeyError:
            fail_safe -= 1
            continue


if __name__ == '__main__':
    open_random_comic()
