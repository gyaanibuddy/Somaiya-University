# Find the complete Problem statement, and assignment at -
# https://www.gyaanibuddy.com/assignments/assignment-detail/basic-socket-programming/
# server.py 

import socket
 
def serverLogic():
    ss = socket.socket()  
    ss.bind((socket.gethostname(), 5000))  
    ss.listen(2)
    clt,adr= ss.accept()  
    print("Connection established")
    while True:
        msg = clt.recv(1024).decode()
        if not msg:
            break
        print("Received from client:" + str(msg))
        msg = input('Enter reply:')
        clt.send(msg.encode()) 
    clt.close() 
if __name__ == '__main__':
    serverLogic()


# client.py

import socket
 
def clientLogic():
    sc = socket.socket()  
    sc.connect((socket.gethostname(),5000))  
    msg = input("Enter message:") 
    while msg!= 'end':
        sc.send(msg.encode())  
        data = sc.recv(1024).decode()  
        print('Received from server: ' + data)  
        msg = input("Enter message:")  
    sc.close()  
if __name__ == '__main__':
    clientLogic()
