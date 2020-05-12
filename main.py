from timer import Timer



HOURS = 0
MINUTES = 0
SECONDS = 10


def main():
    timer = Timer(HOURS, MINUTES, SECONDS)
    timer.run()


if __name__ == '__main__':
    main()