def run_main_file():
    value = 10
    while True:
        print(value)
        value -= 1
        assert (value >= 0),"cant go under 0"


if __name__ == '__main__':

    while True:

        run_main_file()
