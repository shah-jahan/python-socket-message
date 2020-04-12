import socket
from time import sleep

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.43.148', 9986))
print("connected")
while True:
    data = input("Enter message: ")
    if(data == "quit"):
        clientsocket.send(data.encode())
        sleep(0.5)
        exit(0)
    else:
        clientsocket.send(data.encode())
        rply_data = clientsocket.recv(1024)
        print(rply_data)