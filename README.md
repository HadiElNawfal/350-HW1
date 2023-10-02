# Client-ProxyServer

[Server](#Server)
[Client](#Client)

### Server:
Listen on a port that you specify to receive incoming connections.
Analyze the incoming request to extract the destination server's IP address.
Generate a message detailing the request, including the IP address and the exact time it was made.
Forward the client's request to the destination server.
Record the exact time when the actual request was made and print a corresponding message.
Receive the response from the destination server.
Display a message indicating the successful reception of the response along with the exact time.
Send the response back to the client.
Print a message confirming the response has been sent, including the exact time.
If any errors occur either on the client's or server's end, the proxy server should notify the user and return an error message to the client.

### Client:
Accept input for the IP address of the website you want to access.
Send the request to the proxy server.
Print a message displaying the request details and the exact time it was sent.
Receive the reply from the proxy server and present it to the user, indicating the exact time it was received.
Calculate and show the total round-trip time.
Display your physical MAC address (not the one from the virtual machine).
Please note that the assignment will not be considered complete without displaying the MAC address.
