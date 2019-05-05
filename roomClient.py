# -*- coding: utf-8 -*-
"""

@author: mohmd farag
"""
#socket module
from socket import socket, AF_INET, SOCK_STREAM
#thread module
from threading import *
#TKinter GUI module
from tkinter import *
from tkinter import Tk
from tkinter import messagebox , Button , Label 
#Object of TK fun

window = Tk()
window.title(" Chat App ")#title of window
window.geometry("500x400")  #dimentions

label = Label(window)
label.grid(row=3 ,column=3)


entry = Entry(window, width="50")
entry.grid(row=1 ,column=3)
def clicked():
    msg= entry.get()
    s.send(msg.encode('UTF-8'))
    entry.delete(0, END)
    
btn = Button(window,text="Send" ,bg="red",fg="white", width=9, height=1 ,command=clicked)
btn.grid(row=1 ,column=5)


def Receive(s):
    while True:
        x=s.recv(1024)
        label['text'] += "\n" + x.decode('UTF-8')

s=socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1',7020))
receive=Thread(target=Receive,args=(s,))
receive.start()

window.mainloop()