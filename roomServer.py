# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:04:27 2019

@author: lenovo
"""

from socket import *
from _thread import *
from threading import *

s= socket(AF_INET,SOCK_STREAM) #(family ipv4 , protocol TCP)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#ip address
host= "127.0.0.1" 
#port number
port= 7020
s.bind((host,port))#(())>>vector data type
#no. of request
s.listen(20)

clients=[]

def sendToAll(c , ad):
    while True:
        message = str(ad[1])+" : "+c.recv(1048).decode("UTF-8")
        for client in clients:
            if client != c :
                client.send(message.encode('UTF-8'))
            

    

        
while True:
    c,ad=s.accept()
    msg ="new connection from >> "+str(ad[1])
    for session in clients:
        session.send(msg.encode('utf-8'))
    clients.append(c)
    start_new_thread(sendToAll ,(c,ad))