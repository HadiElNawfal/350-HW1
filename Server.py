#Server Code

#the following imports for socket, time, and threading, threading idea and codes mostly inspired from geeksforgeeks.org
import socket
import time
import threading

#server and handling the request are 2 separate functions
def Server():
    #set up server socket
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)#gethostname() function from pythontic.com
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = (ipAddress, 8080)
    serverSocket.bind(serverAddress)
    serverSocket.listen()#server socket and server address lines from realpython.com

    print("Proxy server is running on", serverAddress)

    while True:
        #accept incoming client connection
        clientSocket, clientAddress = serverSocket.accept()
        print(f"Accepted connection from {clientAddress}",time.time())

        #start a new thread to handle the request
        t = threading.Thread(target=handleRequest, args=(clientSocket, clientAddress))
        t.start()

def handleRequest(clientSocket, clientAddress):
    try:
        #listen on a port for incoming connections and parse request
        request = clientSocket.recv(4096).decode()
        print(f"Request from {clientAddress}: {request}",time.time())
        #send the client's request to the destination server
        startIndex = request.find("Host:") + 6
        endIndex = request.find("\r\n", startIndex)
        destIP = socket.gethostbyname(request[startIndex:endIndex])
        print(f"Destination IP: {destIP}",time.time())

        #send request to destination server
        destPort = 80
        socketD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketD.connect((destIP, destPort))
        socketD.sendall(request.encode())

        #receive the response from the destination server 
        response = socketD.recv(4096)
        print(f"Response from {destIP}: {response.decode()}",time.time())

        #send the response back to the client
        clientSocket.sendall(response)
        
#If there was any error from the client side or from the server side, the proxy server
#should display a message and return an error message to the client 
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        #close server socket
        clientSocket.close()
        socketD.close()

if __name__ == "__main__":
    Server()#geeksforgeeks.org
