# Create a Python program that:
# imports socket
# connects to a web server
# sends a valid HTTP GET request
#BEGIN
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("example.com", 80))
request = ("GET / HTTP/1.1\r\n" "Host: example.com\r\n""Connection: close\r\n""\r\n")
client.sendall(request.encode())
response = client.recv(4096)
print(response.decode())
client.close()
#END



# Task 2: Extend the program so it:
# repeatedly calls recv(512)
# decodes each chunk
# prints the full response
# closes the socket after all data is received
#BEGIN
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("example.com", 80))

request = ("GET / HTTP/1.1\r\n"
           "Host: example.com\r\n"
           "Connection: close\r\n"
           "\r\n")
client.sendall(request.encode())
response = ""
while True:
    data = client.recv(512)
    if not data:
        break
    response += data.decode()
print(response)
client.close()
#END


# Task 3: Real-World
# Build a simple webpage fetcher that:
# accepts a URL (host and path)
# opens a socket to port 80
# sends an HTTP GET request
# receives the response
# separates the headers from the HTML body
# displays both sections
#BEGIN
import socket
host = input("Enter the host address: ")
path = input("Enter the path: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 80))
request = (f"GET /{path} HTTP/1.1\r\n"
           f"Host: {host}\r\n"
           "Connection: close\r\n"
           "\r\n"
           )
sock.sendall(request.encode())

response = ""

while True:
    data = sock.recv(4096)
    if not data:
        break
    response += data.decode()

sock.close()

headers, body = response.split("\r\n\r\n", 1)

print("\n--- HEADERS ---\n")
print(headers)

print("\n--- BODY ---\n")
print(repr(body))
#END


