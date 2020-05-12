from timer import Timer
from gui import GUI



HOURS = 0
MINUTES = 2
SECONDS = 10


def main():
    timer = Timer(HOURS, MINUTES, SECONDS)
    gui = GUI(timer)


if __name__ == '__main__':
    main()