# Client-ProxyServer


This README provides instructions on how to run the Client and Proxy Server codes.

## Table of Contents

 [Client-Proxy Server](#Client-ProxyServer)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
    - [Running the code](#running-the-code)

## Installation

### Prerequisites

Before installing Scapy, make sure you have the following prerequisites:

1. **Python**: Scapy requires Python 3.x. Make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Pip**: Pip is the package manager for Python. It's usually included with Python, so you should have it available. You can check if Pip is installed by running `pip --version` in your terminal/command prompt.

### Installation Steps

1. Through your terminal or command prompt, install Scapy using pip by running the following command: `pip install scapy`


    This will download and install Scapy and its dependencies.


2. You can clone both codes, once the installation is complete, using the command: git clone https://github.com/Client-ProxyServer

## Server:
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

## Client:
* Accepts input for the IP address of the website you want to access.
* Sends the request to the proxy server.
* Prints a message displaying the request details and the exact time it was sent.
* Receives the reply from the proxy server and present it to the user, indicating the exact time it was received.
* Calculates and shows the total round-trip time.
* Displays the user's physical MAC address (not the one from the virtual machine).

