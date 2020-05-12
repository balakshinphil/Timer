from time import sleep



class Timer():

    def __init__(self):
        hours = 0
        minutes = 5
        seconds = 0

        self._time = hours * 3600 + minutes * 60 + seconds
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds


    def get_time_string(self):
        hours = str(self.hours) if self.hours > 9 else '0' + str(self.hours)
        minutes = str(self.minutes) if self.minutes > 9 else '0' + str(self.minutes)
        seconds = str(self.seconds) if self.seconds > 9 else '0' + str(self.seconds)

        return hours + ' : ' + minutes + ' : ' + seconds


    def update_time(self):
        self._time = self._hours * 3600 + self._minutes * 60 + self._seconds


    def decrease_time(self):
        self._time -= 1

    
    def increase_hours(self):
        self._hours += 1
        self.update_time()


    def decrease_hours(self):
        self._hours -= 1
        self.update_time()

    
    def increase_minutes(self):
        self._minutes += 1
        self.update_time()


    def decrease_minutes(self):
        self._minutes -= 1
        self.update_time()


    def increase_seconds(self):
        self._seconds += 1
        self.update_time()


    def decrease_seconds(self):
        self._seconds -= 1
        self.update_time()


    @property
    def time(self):
        return self._time;


    @property
    def hours(self):
        return self._time // 3600


    @hours.setter
    def hours(self, hours):
        self._hours = hours
        self.update_time()


    @property
    def minutes(self):
        return (self._time - self.hours * 3600) // 60

    
    @minutes.setter
    def minutes(self, minutes):
        self._minutes = minutes
        self.update_time()


    @property
    def seconds(self):
        return self._time - self.hours * 3600 - self.minutes * 60


    @seconds.setter
    def seconds(self, seconds):
        self._seconds = seconds
        self.update_time()
