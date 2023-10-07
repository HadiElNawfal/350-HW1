# Client-ProxyServer

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

