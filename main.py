from tkinter import Tk
from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
from tkinter import filedialog
import os

root = Tk()

mixer.init()
test1 = open("test.txt","r+")
print(test1)

def play(name):
    mixer.music.load(name)
    print(name)
    mixer.music.play()
    pb.start

def stop():
    mixer.music.pause()

def select():
    directory = os.getcwd()
    filename = filedialog.askopenfilename(initialdir= directory, title="Select a File",filetypes=(("Music files", "*.mp3 .wav*"), ("all files", "*.*")),initialfile = "Untitled")
    play(filename)
    file = open("test.txt","w+")
    file.write(filename)
    file.close()
pb = Progressbar(root, orient='horizontal', mode='indeterminate',length=28)
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