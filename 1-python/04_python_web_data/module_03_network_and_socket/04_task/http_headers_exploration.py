# Task : Use Python’s socket library to connect to data.pr4e.org
# , send an HTTP GET request for /intro-short.txt, receive the response,
# and extract and print only the headers
# Last-Modified, ETag, Content-Length, Cache-Control, and Content-Type.
#BEGIN
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("data.pr4e.org", 80))

request = "GET /intro-short.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n"
client.sendall(request.encode())

response = b""

while True:
    data = client.recv(1024)
    if not data:
        break
    response += data

response = response.decode()

# split into headers and body (your requested method)
headers, body = response.split("\r\n\r\n", 1)

# convert headers into lines
header_lines = headers.split("\r\n")

# required fields
fields = [
    "Last-Modified",
    "ETag",
    "Content-Length",
    "Cache-Control",
    "Content-Type"
]

print("=== REQUIRED HEADERS ===")

for line in header_lines:
    for field in fields:
        if line.startswith(field):
            print(line)

client.close()
#END