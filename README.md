# Client-ProxyServer


This README provides instructions on how to run the Client and Proxy Server codes.

## Table of Contents

 [Client-Proxy Server](#Client-ProxyServer)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
  - [Running the Codes](#running-the-codes)
    - [Server](#Server)
    - [Client](#Client)
  - [Limitations and Possible Enhancements](#limitations-and-possible-enhancements)
    - [Limitations](#Limitations)
    - [Enhancements](#Enhancements)
  - [Sample Client Output](#Sample-Client-Output)
  - [Sample Server Output](#Sample-Server-Output)

## Installation

### Prerequisites

Make sure you have the following prerequisites:

1. **Python**: The code requires Python 3.x. Make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Pip**: Pip is the package manager for Python. It's usually included with Python, so you should have it available. You can check if Pip is installed by running `pip --version` in your terminal/command prompt.

### Installation Steps

1. Through your terminal or command prompt, install `getmac` using pip by running the following command:
```
pip install getmac
```
This will download and install getmac and its dependencies.


2. You can clone both codes, once the installation is complete, using the command:
```
git clone https://github.com/HadiElNawfal/Client-ProxyServer
```

## Running the Codes
1. Run the Server code by typing the following in a terminal in the file's directory:
```
python Server.py
```

2. Run the Client code by typing the following in a terminal in the file's directory:
```
python Client.py
```
### Server:
The script:
* Listens on a port that is specified to receive incoming connections.
* Analyzes the incoming request to extract the destination server's IP address.
* Generates a message detailing the request, including the IP address and the exact time it was made.
* Forwards the client's request to the destination server.
* Records the exact time when the actual request was made and prints a corresponding message.
* Receives the response from the destination server.
* Displays a message indicating the successful reception of the response along with the exact time.
* Sends the response back to the client.
* Prints a message confirming the response has been sent, including the exact time.
* If any errors occur either on the client's or server's end, the proxy server notifies the user and returns an error message to the client.

### Client:
The script:
* Accepts input for the IP address of the website you want to access.
* Sends the request to the proxy server.
* Prints a message displaying the request details and the exact time it was sent.
* Receives the reply from the proxy server and present it to the user, indicating the exact time it was received.
* Calculates and shows the total round-trip time.
* Displays the user's physical MAC address (not the one from the virtual machine).

## Limitations and Possible Enhancements
### Limitations
* Lack of Encryption: The current implementation does not use TLS, meaning data is sent in plain text and is susceptible to interception.
* Basic Error Handling: While the proxy notifies on errors, there is no comprehensive mechanism to recover or retry failed requests automatically.
* Single-Client Focus: The code may need manual scaling to manage larger loads.

### Enhancements
* Add HTTPS/TLS Support: Implement secure connections by integrating SSL/TLS, ensuring data is encrypted and secure in transit.
* Multi-Threading or Async Support: Enable the server to manage multiple simultaneous client connections.
* Logging and Analytics: Integrate more detailed logging, storing logs in a database for future analysis.

## Sample Client Output
```
MAC Address: f0:20:ff:21:ed:50
Enter website IP: 8.8.8.8  
Request sent to ('192.168.127.1', 8080): GET / HTTP/1.1
Host: 8.8.8.8


Response received from ('192.168.127.1', 8080): 
Round-trip time: 21.024 seconds
```

## Sample Server Output
```
Proxy server is running on ('192.168.127.1', 8080)
Accepted connection from ('192.168.127.1', 55896) 1739481408.4275901
Request from ('192.168.127.1', 55896): GET / HTTP/1.1
Host: 8.8.8.8

 1739481408.429475
Destination IP: 8.8.8.8 1739481408.429475
```
