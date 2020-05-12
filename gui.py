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
            
            self._text.set(str(self._timer.hours) + " : " + str(self._timer.minutes) + " : " + str(self._timer.seconds))
            self._label.pack()
            self._root.update()
            sleep(1)
            self._timer.decrease_time()
        self._text.set(str(self._timer.hours) + " : " + str(self._timer.minutes) + " : " + str(self._timer.seconds))

        wave_obj = sa.WaveObject.from_wave_file("sound.wav")
        play_obj = wave_obj.play()




    def timer_stop(self):
        self._is_stopped = True


    def timer_reset(self):
        self.timer_stop()
        self._timer.reset_time()
        self._text.set(str(self._timer.hours) + " : " + str(self._timer.minutes) + " : " + str(self._timer.seconds))


    def __init__(self, timer):
        self._is_stopped = False
        self._timer = timer

        self._root = tk.Tk()
        self._root.title("Timer")
        self._root.geometry("300x100")

        windowWidth = self._root.winfo_reqwidth()
        windowHeight = self._root.winfo_reqheight()
        positionRight = int(self._root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self._root.winfo_screenheight()/2 - windowHeight/2)
        self._root.geometry("+{}+{}".format(positionRight, positionDown))

        self._text = tk.StringVar()
        self._text.set(str(timer.hours) + " : " + str(timer.minutes) + " : " + str(timer.seconds))

        self._label = tk.Label(self._root, textvariable=self._text)
        self._label.config(font=("Helvetica", 44))
        

        self._start_btn = tk.Button(self._root, text="START", command=self.timer_start, width=8, height=2)
        self._start_btn.place(x=20, y=60)

        self._stop_btn = tk.Button(self._root, text="STOP", command=self.timer_stop, width=8, height=2)
        self._stop_btn.place(x=110, y=60)

        self._reset_btn = tk.Button(self._root, text="RESET", command=self.timer_reset, width=8, height=2)
        self._reset_btn.place(x=200, y=60)

        self._label.pack()
        self._root.mainloop()



    