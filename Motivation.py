import tkinter 
from tkinter import *
import random

motivations = ["You are an A* student","Trust in God in everything you do",
"Your failures grows your success","Keep your 100 % mentality","Nothing is impossible",
"Bring out your inner passion","Go study and ace it like a CEO"]
app = Tk()
app.title("Motivation App")
app.geometry("500x500")

heading = Label(app,text="Motivaton")
heading.pack()

mot = Label(app,text="",font=("Arial",25))
mot.pack()

def motivaton():
   btn.config(text="Next")
   motivate = random.choice(motivations)
   mot.config(text=motivate)
btn = Button(app,text="Start",width="40",height="2",command=motivaton)
btn.pack()

app.mainloop()