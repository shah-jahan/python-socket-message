from time import sleep
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("192.168.43.148", 9986))
serversocket.listen(10)
print("server created")
connection, address = serversocket.accept()
while True:
    
    data = connection.recv(1024).decode()
    if len(data) > 0:
        if (data == "quit"):
            print("quitting")
            connection.close()
            serversocket.close()
        else:
            print("Received: " + data)
            connection.send("Recievde".encode())