import socket
from symbol import pass_stmt
import threading

nickname = input("choose a nickname: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",55523))

def recieve():
    while True:
        try:
            message = client.recv(1024)
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("Error: Purge")
            client.close()
            break
