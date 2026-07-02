Topic: HTTP Request–Response Cycle & Communication Using Python Sockets

This lesson builds directly on Lesson 1 (Network Layers → Socket → Port → Connection).

Concept Chain

Network Layers
      ↓
Socket
      ↓
Connection
      ↓
HTTP Protocol
      ↓
HTTP Request
      ↓
HTTP Response
      ↓
send() / recv()
      ↓
Encode / Decode


CONCEPT BLOCK 1 — HTTP: The Application Protocol
1. Concept Name

HTTP (HyperText Transfer Protocol)

2. Encoding Filter

✔ Essential? → YES

✔ What breaks without it?

You know how to connect, but not what to say after connecting.

✔ Connects to?

sockets
browsers
web servers
APIs
web scraping

Importance: High → Expand.


3. Explanation

A socket only creates a communication channel.

HTTP defines the language used over that channel.
Without HTTP, the server receives random bytes and has no idea what you want.

HTTP defines:
HTTP defines	Meaning
Request format	How the client must ask for something
Response format	How the server must reply
Headers	Extra information about the message
Body	The actual content or data
Status codes	The result of the request (success or error)
Classic HTTP uses TCP, but the newest version (HTTP/3) uses UDP indirectly through QUIC.


CONCEPT BLOCK 2 — URL (Uniform Resource Locator)
1. Concept Name

URL Structure

2. Encoding Filter

✔ Essential? → YES

Without URL structure:

cannot locate resources

Connects to:

HTTP
web servers
browsers
3. Explanation

A URL contains multiple pieces of information.

Example

http://www.example.com/page1.html

Breakdown

http://

Protocol

www.example.com

Host (server)

/page1.html

Resource (document)

Memory Anchor

URL tells "how", "where", and "what".


CONCEPT BLOCK 3 — HTTP GET Request
1. Concept Name

GET Request

2. Encoding Filter

✔ Essential → YES

Without GET:

No document retrieval.

3. Explanation

Once connected...

Client sends

GET /page HTTP/1.0

followed by

(blank line)

That blank line means

"Finished sending request."

Server waits for this before responding.

Memory Anchor
Used to request a server for data (like a webpage) and Blank line finishes the request.


CONCEPT BLOCK 4 — HTTP Response
1. Concept Name
Server Response

2. Encoding Filter

Essential → YES

Without it

No data comes back.

3. Explanation

Server sends two sections.

Headers

Metadata

(blank line)

Body

Actual content

Memory Anchor

Headers describe. Body contains.


CONCEPT BLOCK 5 — Request–Response Cycle
1. Concept Name

HTTP Request–Response Cycle

2. Encoding Filter

Essential → YES

This is the entire web.

3. Explanation

Every webpage follows this cycle.

Browser

↓

Connect

↓

Send GET

↓

Server processes

↓

Response

↓

Browser displays

This repeats every click.

Memory Anchor

Every webpage is just thousands of request–response cycles.


CONCEPT BLOCK 6 — Python send()
1. Concept Name

Sending Data

2. Encoding Filter

Essential → YES

Without send()

Server receives nothing.

3. Explanation
#cmd = "GET /romeo.txt HTTP/1.0\r\n\r\n"

#mysock.send(cmd.encode())

Steps

create request
encode
send

Memory Anchor

send() transmits bytes—not Python strings.

BLOCK 7 — Python recv()
1. Concept Name

Receiving Data

2. Encoding Filter

Essential → YES

Without recv()

Nothing can be read.

3. Explanation
#while True:

    #data = mysock.recv(512)

    #if len(data) < 1:
        #break

    #print(data.decode())

recv()

reads up to

512 bytes

each time.

Eventually

empty bytes

means

End of transmission.

Memory Anchor

recv() reads data in chunks (bytes), and decode() converts those bytes into a string (str).


CONCEPT BLOCK 8 — Encode & Decode
1. Concept Name

Encoding and Decoding Data

2. Encoding Filter

Critical → YES

Without it

Python strings cannot safely travel across networks.

3. Explanation

Humans read

text

Networks send

bytes

So

Before sending

String

↓

encode()

↓

Bytes

After receiving

Bytes

↓

decode()

↓

String

Memory Anchor

Network speaks bytes. Humans speak strings.



Python Program Starts
        │
        ▼
Import socket module
        │
        ▼
Create Socket Object
        │
        ▼
Configure Socket
        │
        ├── Address Family → IPv4 (AF_INET)
        └── Protocol → TCP (SOCK_STREAM)
        │
        ▼
Request Connection (client.connect)
        │
        ▼
DNS Lookup (Domain → IP)
        │
        ▼
Hostname Resolution
example.com → 93.184.216.34
        │
        ▼
TCP Three-Way Handshake
        │
        ├── SYN
        ├── SYN-ACK
        └── ACK
        │
        ▼
TCP Connection Established
        │
        ▼
────────────────────────────────────
        TRANSPORT LAYER READY
────────────────────────────────────
        │
        ▼
Build HTTP Request (Application Layer)
        │
        ├── GET / HTTP/1.1
        ├── Host: example.com
        ├── Connection: close
        └── CRLF (blank line ends headers)
        │
        ▼
Encode HTTP Request (string → bytes)
        │
        ▼
Send Data (client.send)
        │
        ▼
TCP Segmentation
        │
        ├── Break into packets
        ├── Add TCP headers
        └── Send over Internet
        │
        ▼
Server Receives Request
        │
        ▼
Server Processes HTTP Request
        │
        ├── Reads method (GET)
        ├── Reads path (/)
        ├── Reads headers (Host, Connection)
        └── Generates response
        │
        ▼
HTTP Response Created
        │
        ├── Status Line (200 OK)
        ├── Headers (Content-Type, etc.)
        └── Body (HTML page)
        │
        ▼
Response Sent Over TCP
        │
        ▼
Client Receives Data (client.recv)
        │
        ▼
TCP Stream Assembly (bytes chunks)
        │
        ▼
Raw HTTP Response (bytes)
        │
        ▼
Decode Bytes → String (UTF-8)
        │
        ▼
Readable HTTP Output
        │
        ▼
Print to Terminal (print)
        │
        ▼
Program Ends / Connection Closed


REAL-WORLD APPLICATION
Scenario: Building a Minimal Browser

System flow:

User enters http://example.com/index.html
Program extracts the protocol, host, and path.
Creates a socket.
Connects to example.com on port 80.
Sends an HTTP GET request.
Server processes the request.
Server returns headers followed by the HTML body.
Program repeatedly calls recv() until no more bytes remain.
Program decodes and displays the HTML.
Socket is closed.

Key Memory Anchors
Sockets connect; HTTP communicates.
URL = how + where + what.
GET asks; blank line finishes the request.
Headers describe; body contains.
Every webpage is a request–response cycle.
send() sends bytes; recv() receives bytes.
Networks use bytes; people use strings.