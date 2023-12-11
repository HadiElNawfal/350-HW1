#Client Code

#the following imports for socket, time analysis, and mac address
import socket
import time
import uuid
from getmac import get_mac_address

#get physical MAC address
def getMac():
    mac = get_mac_address()
    return mac
macAddress = getMac()
print("MAC Address:", macAddress)

#set up client socket
def client():
    
    #host ipaddress for proxy server
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)#gethostname() function from pythontic.com
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#client socket and proxy address lines from realpython.com
    proxyAddress = (ipAddress, 8080)

    #take as input the website IP to be accessed
    websiteIP = input("Enter website IP: ")

    try:
        #send the request to proxy server
        request = f"GET / HTTP/1.1\r\nHost: {websiteIP}\r\n\r\n"
        starttime = time.time()
        clientSocket.connect(proxyAddress)
        clientSocket.sendall(request.encode())
        print(f"Request sent to {proxyAddress}: {request}")#print a message with the request details and the exact time sent

        #receive response from proxy server
        response = clientSocket.recv(4096)
        endtime = time.time()
 #receive the reply back from the proxy server and display it to the user with the exact time received
        print(f"Response received from {proxyAddress}: {response.decode()}")
        #Calculate and display the total round-trip time
        print(f"Round-trip time: {endtime - starttime:.3f} seconds")
#the above from reqbin.com and scrapingbee.com
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        #close socket
        clientSocket.close()

if __name__ == "__main__":
    client()#from geeksforgeeks.org
