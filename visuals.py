import sys

def main_menu():
    while True:
        print('What do you want to do?')
        print('''
    1. Download all comic images from xkcd.com to your hard drive
    2. Chose a comic to open from the website xkcd.com
    3. Exit
''')
        choice = input()
        if choice.isdecimal() and int(choice) >= 1 and int(choice) <= 3:
            return int(choice)

def line_separator(arg): # for printing separation lines in terminal
    if arg == 'start':
        print("\n---------------------")
    elif arg == 'end':
        print("---------------------")
    else:
        return None

def up_lines(N):
    for i in range(N):
        sys.stdout.write("\033[F")

def loading_bar(count,total):
    if total >= 100:
        progress = total/100
        step = total/50
        base = 0.0
        N = -1
        while count > int(base):
            N += 1
            base += progress

        percentage = N

        base = 0
        N = -1
        while count > int(base):
            N += 1
            base += step
        symbol = ''
        symbol = '|' * N

        if percentage <= 0:
            percentage = 0
        if percentage >= 100:
            percentage = 99
        print(f'{percentage}%')
        print(symbol.ljust(50, '-'))
        up_lines(2)
        if count == total:
            print('100%')
            print(symbol.ljust(50, '|'))
            up_lines(2)
            print('\n\nDone\n')
    elif total >= 10:
        progress = total/10
        step = total/10
        base = 0.0
        N = 0
        while count > int(base):
            N += 10
            base += progress
        percentage = N
        base = 0
        N = 0
        while count > int(base):
            N += 1
            base += step
        symbol = ''
        symbol = '|' * N

        print(f'{percentage}%')
        print(symbol.ljust(10, '-'))
        up_lines(2)
        if count == total:
            print('\n\nDone\n')
    else:
        if count == total:
            print('\n\nDone\n')
        else:
            print('Working..')
            up_lines(1)
