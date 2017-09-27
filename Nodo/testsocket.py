import socket
from time import sleep


host = "192.168.0.6"
port = 5001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

# Main Functionality
while 1:
    data = "caca"
    s.send(data)
    sleep(3)
    