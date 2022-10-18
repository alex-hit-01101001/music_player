from tkinter import Tk
from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
from tkinter import filedialog
import os

root = Tk()



mixer.init()
mixer.music.load("C:/Users/panos/Downloads/disturbed.mp3")

def play():
    mixer.music.play()
    pb.start

def stop():
    mixer.music.pause()

def select():
    directory = os.getcwd()
    filename = filedialog.askopenfilename(initialdir= directory, title="Select a File",
                                          filetypes=(("Music files", "*.mp3 .wav*"), ("all files", "*.*")),
                                          initialfile = "Untitled")

pb = Progressbar(root, orient='horizontal', mode='indeterminate',length=280)
pb.pack()

def resume():
    mil = (mixer.music.get_pos() / 1000)
    seconds = int(mil)
    print(seconds)
    pb['value'] += seconds
    mixer.music.unpause()

select1 = Button(root , text = "select" , command = select)
select1.pack()

button = Button(root , text = "play" , command= play)
button.pack()

button = Button(root , text = "stop" , command= stop)
button.pack()

button = Button(root , text = "resume" , command= resume)
button.pack()

root.mainloop()