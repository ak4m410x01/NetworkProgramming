from socket import *
from threading import *

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("127.0.0.1", 55555)
CLIENT_NAME = input("Name:")

# Create Socket Connection
client_socket_connection = socket(AF_INET, SOCK_STREAM)

# Connect with Server Addr
client_socket_connection.connect(SERVER_ADDR)


def recive() -> None:
    while True:
        try:
            # Recv Message from Server
            client_msg = client_socket_connection.recv(MAX_BUFFER_SIZE).decode("ASCII")

            if client_msg == "name":
                # Send Name to server
                client_socket_connection.sendall(CLIENT_NAME.encode("ASCII"))

            else:
                print(client_msg)

        except error:
            print(error)

            client_socket_connection.close()
            break


def send() -> None:
    while True:
        try:
            # Read & Send Data to Server
            client_msg = input()
            client_socket_connection.sendall(client_msg.encode("ASCII"))

        except error:
            print(error)


receive_thread = Thread(target=recive).start()

send_thread = Thread(target=send).start()
