from tkinter import *
from tkinter import ttk
import tkinter
import  _tkinter


root= Tk()
def key_press(event):
    print("type:{}".format(event.type))
def button_press(event):
    print("button pressed")
bu=ttk.Button(root,text="Click me")
bu.pack()
bu.bind("<ButtonPress>",button_press)
root.bind("<Control-c>",key_press)
root.mainloop()