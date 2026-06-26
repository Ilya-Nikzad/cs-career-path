# Task 1: Create a socket and connects to example.com on port 80
#BEGIN
import socket
host = "example.com"
infos = socket.getaddrinfo(host, 80)
for info in infos:
    print(info)



