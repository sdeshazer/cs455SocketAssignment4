# import socket module
from socket import *
import sys  # In order to terminate the program

def web_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    serverPort = 8000
    serverHost = '0.0.0.0'
    serverSocket.bind((serverHost, serverPort ))
    serverSocket.listen(1)

    while True:
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        try:
            message =
            filename = message.split()[1]
            file = open(filename[1:])
            outputdata =

            # Send one HTTP header line into socket
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()
            except IOError:

                # Send response message for file not found
                # Close client socket

        serverSocket.close()

        sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    web_server()