#!/usr/bin/env python3
from download_comics import download
from build_database import build_comic_db
from visuals import main_menu

def run_main_file():

    choice = main_menu()
    build_comic_db()
    if choice == 1: # download all comics
        download()
    elif choice == 2: # chose from all comics
        print('2')
    elif choice == 3: # open random comic
        print('3')
        exit()
    elif choice == 4: # Exit
        print('\t\t\tExiting..')
        exit()
if __name__ == '__main__':


    run_main_file()
