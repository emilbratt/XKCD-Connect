#!/usr/bin/env python3
from download_comics import download
from build_database import build_comic_db
from visuals import main_menu, up_lines
from database_client import database
from open_random import open_random_comic

def run_main_file():
    database()
    build_comic_db()

    while True:

        choice = main_menu()
        if choice == 1: # download all comics
            download()
        elif choice == 2: # chose from all comics
            print('2')
        elif choice == 3: # open random comic
            open_random_comic()
        elif choice == 4: # Exit
            print('\t\t\tExiting..')
            exit()

if __name__ == '__main__':


    run_main_file()
