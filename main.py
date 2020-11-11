#!/usr/bin/env python3
from download_comics import download
from build_database import build_comic_db
from visuals import main_menu

def run_main_file():

    choice = main_menu()
    if choice == 1:
        build_comic_db()
        download()
    elif choice == 2:
        build_comic_db()
        print('2')
    elif choice == 3:
        print('Exiting..')
        exit()


if __name__ == '__main__':


    run_main_file()
