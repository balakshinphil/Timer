from time import sleep



class Timer():
    time = 0


    def __init__(self, hours, minutes, seconds):
        self.time = hours * 3600 + minutes * 60 + seconds


    def __printTime(self):
        hours = self.time // 3600
        minutes = (self.time - hours * 3600) // 60
        seconds = self.time - hours * 3600 - minutes * 60
        print('\b' * 12 + ' ' * 12 + '\r', end='')
        print(str(hours) + " : " + str(minutes) + " : " + str(seconds), end='')
        

    def run(self):
        while(self.time > 0):
            self.__printTime()
            self.time -= 1
            sleep(1)
        print('\b' * 12 + ' ' * 12 + '\r', end='')    
        print('0 : 0 : 0')
