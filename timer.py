from time import sleep



class Time():

    def __init__(self, hours, minutes, seconds):
        self._time = hours * 3600 + minutes * 60 + seconds
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def update(self):
        self._hours = self._time // 3600
        self._minutes = (self._time - hours * 3600) // 60
        self._seconds = self._time - hours * 3600 - minutes * 60


    def decrease_time(self):
        self._time -= 1

    
    def increase_time(self):
        self._time += 1

    @property
    def time(self):
        return self._time;

    
    @property
    def hours(self):
        return self._hours


    @property
    def minutes(self):
        return self._minutes


    @property
    def seconds(self):
        return self._seconds


    # def __clean_line(self):
    #     print('\b' * 12 + ' ' * 12 + '\r', end='')


    # def __print_time(self):
    #     hours = self._time // 3600
    #     minutes = (self._time - hours * 3600) // 60
    #     seconds = self._time - hours * 3600 - minutes * 60
    #     self.__clean_line()
    #     print(str(hours) + " : " + str(minutes) + " : " + str(seconds), end='')
        

    # def run(self):
    #     while(self._time > 0):
    #         self.__print__time()
    #         self._time -= 1
    #         sleep(1)
    #     self.__clean_line()    
    #     print('0 : 0 : 0')
