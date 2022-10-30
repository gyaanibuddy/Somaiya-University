# Find the complete Problem statement, and assignment at -
# https://www.gyaanibuddy.com/assignments/assignment-detail/go-back-n-using-socket/

# sender.py 

import socket
import time
from random import *
HOST = '127.0.0.1'
PORT = 2020
 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
connection, addr = s.accept()
s.settimeout(10.0)
print('Connection established!!!')
 
m=int(input("Enter value of m:"))
Sw=2**m-1
Sf=0
Sn=0
total_frames=int(input("Enter number of frames to be sent:"))
seq=[str(i) for i in range(total_frames)]
 
connection.send(bytes(str(m), "utf-8"))
ack = connection.recv(512).decode("utf-8")
 
while True:
    if Sf==total_frames:
        connection.send(bytes("End", "utf-8"))
        print("All Frames transmitted")
        break
    sent = randint(0, 1)
    if Sn-Sf<Sw and Sn<total_frames:#when window not full
        if sent == 1:
            connection.send(bytes(seq[Sn], "utf-8"))
            print("Frame", int(seq[Sn])%(Sw+1), "Sent")
            Sn+=1
            ack = connection.recv(512).decode("utf-8")
            if ack != "Lost ACK" and ack!= "No ACK":
                if int(ack) > Sf and int(ack) <= Sn:#valid ack
                    print("Ack", int(ack) % (Sw + 1),"received")
                    while Sf < int(ack):#cumulative ack ,purge frame                       
                        Sf += 1
        else:
            connection.send(bytes("Frame Lost", "utf-8"))
            print("Frame", int(seq[Sn]) % (Sw + 1), "Lost")
            Sn += 1
    else:
        print("Timeout!Resending the frames again")
        for i in range(Sf, Sn):
            print("Frame", int(seq[i]) % (Sw + 1), "resent")
            connection.send(bytes("R"+seq[Sf], "utf-8"))
            Sf += 1
            ack = connection.recv(512).decode("utf-8")
            if ack != "No ACK":
                print("Ack", int(ack) % (Sw + 1), "received")               
                while Sf < int(ack):         
                    Sf += 1   
    time.sleep(1)
 


# receiver.py


import socket
import time
from random import *
 
HOST = '127.0.0.1'  
PORT = 2020      
 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(10.0)
 
m= int(s.recv(512).decode("utf-8"))
window=2**m
s.send(bytes("Got m", "utf-8"))
 
Rn=0
while True:
    try:
        msg= s.recv(512).decode("utf-8")
    except:
        msg=""
        print("Sender didnt send frame")
    if msg=="End":
        print("All Frames received")
        break
    if not (msg == "Frame Lost" or msg == ""):
        if msg[0]=="R":
            msg=msg[1:]
            ack=1
        else:
            ack=randint(0,1)
        if msg==str(Rn):#if expected frame
            print("Frame",int(msg)%window,"received")
            Rn+=1#slide window
            if ack==1:
                print("Ack Sent")
                s.send(bytes(str(Rn),"utf-8"))
            else:
                print("Ack Lost")
                s.send(bytes("Lost ACK", "utf-8"))
        else:
            s.send(bytes("No ACK", "utf-8"))
            print("Frame", int(msg)%window,"recevied but discarded since out of order")       
    time.sleep(1)

