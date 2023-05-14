from socket import *

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("127.0.0.1", 55555)


class DestinationError(Exception):
    def __str__(self) -> str:
        return f"{self.args[0]}"


# Create Socket Connection
client_socket_connection = socket(AF_INET, SOCK_STREAM)

# set timeout = 5
client_socket_connection.settimeout(2)

try:
    # Connect with Server
    client_socket_connection.connect(SERVER_ADDR)

    # Send Data To Server
    client_msg = "Hi, Server".encode()
    client_socket_connection.sendall(client_msg)

    print(f"Send To `{SERVER_ADDR}: Message => {client_msg.decode()}`")

    try:
        # Recv Data From Server
        server_msg = client_socket_connection.recv(MAX_BUFFER_SIZE)

        print(f"Received From `{SERVER_ADDR}: Message => {server_msg.decode()}`")

    except timeout:
        print(DestinationError(f"received timeout: {timeout.strerror}"))

    # Close
    client_socket_connection.close()

except error:
    client_socket_connection.close()

    print(error)
