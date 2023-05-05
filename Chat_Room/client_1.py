import socket
import threading

MAX_BUFFER_SIZE = 1024

CLIENT_NAME = input("Name:")


def connection_close() -> None:
    print("*****************************************")
    print(f" {CLIENT_NAME}  Connection Closed :(    ")
    print("*****************************************")


def recv_message() -> None:
    while True:
        try:
            _server_msg = _client_connection_socket.recv(MAX_BUFFER_SIZE).decode(
                "ASCII"
            )

            if _server_msg == "Name:":
                _client_connection_socket.sendall(CLIENT_NAME.encode("ASCII"))
            else:
                print(_server_msg)

        except:
            print("Client recv message error... :(")

            connection_close()

            _client_connection_socket.close()
            break


def send_message() -> None:
    while True:
        try:
            _client_msg = input().encode("ASCII")

            _client_connection_socket.sendall(_client_msg)
        except:
            print("Client send message error... :(")

            connection_close()

            _client_connection_socket.close()
            break


server_ip = socket.gethostbyname(socket.gethostname())
server_port = 55555

# Create TCP Socket Connection
_client_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect with Server
_server_addr = (server_ip, server_port)
_client_connection_socket.connect(_server_addr)

# Recv thread...
recv_thread = threading.Thread(target=recv_message)
recv_thread.start()

# Send thread...
send_thread = threading.Thread(target=send_message)
send_thread.start()
