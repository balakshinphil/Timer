import tkinter as tk
from timer import Timer
from time import sleep
import simpleaudio as sa



class GUI():
    def timer_start(self):
        self._is_stopped = False

        while self._timer.time > 0:
            if self._is_stopped:
                return
            
            self._text.set(self._timer.get_time_string())
            self._root.update()
            sleep(1)
            self._timer.decrease_time()
        self._text.set(self._timer.get_time_string())

        wave_obj = sa.WaveObject.from_wave_file("sound.wav")
        play_obj = wave_obj.play()


    def timer_stop(self):
        self._is_stopped = True


    def timer_reset(self):
        self.timer_stop()
        self._timer.update_time()
        self._text.set(self._timer.get_time_string())


    def increase_hours(self):
        if self._timer.hours == 24:
            self._timer.hours = 0
        else:
            self._timer.increase_hours()
        self._text.set(self._timer.get_time_string())


    def decrease_hours(self):
        if self._timer.hours == 0:
            self._timer.hours = 24
        else:
            self._timer.decrease_hours()
        self._text.set(self._timer.get_time_string())


    def increase_minutes(self):
        if self._timer.minutes == 59:
            self._timer.minutes = 0
        else:
            self._timer.increase_minutes()
        self._text.set(self._timer.get_time_string())


    def decrease_minutes(self):
        if self._timer.minutes == 0:
            self._timer.minutes = 59
        else:
            self._timer.decrease_minutes()
        self._text.set(self._timer.get_time_string())


    def increase_seconds(self):
        if self._timer.seconds == 59:
            self._timer.seconds = 0
        else:
            self._timer.increase_seconds()
        self._text.set(self._timer.get_time_string())


    def decrease_seconds(self):
        if self._timer.seconds == 0:
            self._timer.seconds = 59
        else:
            self._timer.decrease_seconds()
        self._text.set(self._timer.get_time_string())



    def __init__(self):
        self._is_stopped = False
        self._timer = Timer()


        self._root = tk.Tk()
        self._root.title("Timer")
        self._root.geometry("300x150")
        self._root.resizable(width=False, height=False)


        windowWidth = self._root.winfo_reqwidth()
        windowHeight = self._root.winfo_reqheight()
        positionRight = int(self._root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self._root.winfo_screenheight()/2 - windowHeight/2)
        self._root.geometry("+{}+{}".format(positionRight, positionDown))


        self._text = tk.StringVar()
        self._text.set(self._timer.get_time_string())


        self._label = tk.Label(self._root, textvariable=self._text)
        self._label.config(font=("Helvetica", 44))
        self._label.place(x=35, y=20)
        

        self._start_btn = tk.Button(self._root, text="START", command=self.timer_start, width=8, height=2)
        self._start_btn.place(x=20, y=100)

        self._stop_btn = tk.Button(self._root, text="STOP", command=self.timer_stop, width=8, height=2)
        self._stop_btn.place(x=110, y=100)

        self._reset_btn = tk.Button(self._root, text="RESET", command=self.timer_reset, width=8, height=2)
        self._reset_btn.place(x=200, y=100)

        self._increase_hours_btn = tk.Button(self._root, text="▲", command=self.increase_hours)
        self._increase_hours_btn.place(x=55, y=5)

        self._decrease_hours_btn = tk.Button(self._root, text="▼", command=self.decrease_hours)
        self._decrease_hours_btn.place(x=55, y=70)

        self._increase_minutes_btn = tk.Button(self._root, text="▲", command=self.increase_minutes)
        self._increase_minutes_btn.place(x=140, y=5)

        self._decrease_minutes_btn = tk.Button(self._root, text="▼", command=self.decrease_minutes)
        self._decrease_minutes_btn.place(x=140, y=70)

        self._increase_seconds_btn = tk.Button(self._root, text="▲", command=self.increase_seconds)
        self._increase_seconds_btn.place(x=225, y=5)

        self._decrease_seconds_btn = tk.Button(self._root, text="▼", command=self.decrease_seconds)
        self._decrease_seconds_btn.place(x=225, y=70)


        self._root.mainloop()
