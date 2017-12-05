#CvT 2017 All rights reserved.
#Imports
import webbrowser
import pygame
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from datetime import datetime
from random import randint
from tkinter import Tk
pygame.init()
#vars
window = Tk()
c = Canvas(window, width=900, height=500)
window.title("CvT OS")
date = datetime.now()
music = pygame.mixer.Sound("dubstep.wav")
piano = pygame.mixer.Sound("sounds/piano.wav")
title = Label(window, text="Cvt OS", bg="green", fg="black")
title.pack(fill=X)
dateLabel = Label(window, text=date, fg="black")
dateLabel.pack(side=BOTTOM)
#functions
def ms():
    import ms
def paint():
    import paint
def quit():
    window.destroy()
    quit()
#Welcome message
message = "Welcome"
meh = Label(window, text=message, font='size, 40', fg="orange")
meh.pack()
def change():
    text = askstring("CvT", "Whats the message?")
    meh.config(text=text)
changeb = Button(window, text="Change Message", command=change)
changeb.pack()
def notes():
    note = askstring("CvT", "Type your note in the area below.")
    noteL = Label(window, text=note, bg="red", fg="orange")
    noteL.pack(fill=X)
def bing():
    webbrowser.open("https://www.bing.com/")
def sound():
    chosensong = askstring("CvT", "Choose a song from your playlsit (System)")
    if chosensong == "1":
        music.stop()
        piano.stop()
        music.play()
    elif chosensong == "2":
        music.stop()
        piano.stop()
        piano.play()
def about():
    showinfo("CvT", "This is OS 1.0")
def songplaylist():
    showinfo("CvT", "Here are your songs which you can type into  CvT sounds and they will magicly play.")
    showinfo("CvT", "1: Dubstep")
    showinfo("CvT", "2: Piano")
def CvTGames():
    import ms
def changep():
    with open("passwords.txt", "w") as saves:
        newp = askstring("CvT", "Whats your new password?")
        saves.write(newp)
#menu vars
menu = Menu(window)
window.config(menu=menu)
subMenu = Menu(menu)
subMenu1 = Menu(menu)
#menus
menu.add_cascade(label="System", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)
subMenu.add_command(label="Change Password", command=changep)
subMenu.add_command(label="About", command=about)
subMenu.add_command(label="Songs", command=songplaylist)
menu.add_cascade(label="Applications", menu=subMenu1)
subMenu1.add_command(label="CvT Sounds", command=sound)
subMenu1.add_command(label="CvT Notes", command=notes)
subMenu1.add_command(label="CvT Paint", command=paint)
subMenu1.add_command(label="Meteor Shower", command=CvTGames)
subMenu1.add_command(label="Bing", command=bing)
#run
c.pack()
window.mainloop()
