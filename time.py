from time import sleep



class Timer():

    def __init__(self, hours, minutes, seconds):
        self._time = hours * 3600 + minutes * 60 + seconds

    @property
    def time(self):
        print("Getter")
        return self._time;


    def __clean_line(self):
        print('\b' * 12 + ' ' * 12 + '\r', end='')


    def __print_time(self):
        hours = self._time // 3600
        minutes = (self._time - hours * 3600) // 60
        seconds = self._time - hours * 3600 - minutes * 60
        self.__clean_line()
        print(str(hours) + " : " + str(minutes) + " : " + str(seconds), end='')
        

    def run(self):
        while(self._time > 0):
            self.__print__time()
            self._time -= 1
            sleep(1)
        self.__clean_line()    
        print('0 : 0 : 0')
