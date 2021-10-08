# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 18:27:08 2021

@author: mx
"""

from tkinter import *

root=Tk()
root.title("ASCII")
root.geometry("400x400")
root.configure(background='snow')

enter_word=Entry(root,bg="blue",fg="white")
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label=Label(root,text="name in Ascii :",bg="yellow",fg="black")
label.place(relx=0.5,rely=0.6,anchor=CENTER)

def asciiconverter():
    input_word=enter_word.get()
    
    for letter in input_word:
        label["text"]+=str(ord(letter))+" "
        
btn=Button(root,text="show name in ascii ",command=asciiconverter,bg="grey",fg="black")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()