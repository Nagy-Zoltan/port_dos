import socket
import time

#gets local ip reliably, also cross platform
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()


sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(65535)]


for port, s in enumerate(sockets, 1):
    try:
        s.bind((ip, port))
        s.listen()
    except:
        pass

while True: 
    time.sleep(10)
