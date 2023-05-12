from socket import *

SERVER_ADDR = ("0.0.0.0", 55555)
MAX_BUFFER_SIZE = 1024

# Create Socket Connection
client_socket_connection = socket(AF_INET, SOCK_DGRAM)

# Set Sock option BROADCAST = 1
client_socket_connection.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

try:
    # Send Data to Server...
    client_msg = "Hi, Server... :)".encode()
    client_socket_connection.sendto(client_msg, SERVER_ADDR)

    print(f"Send To `{SERVER_ADDR}`: Message `{client_msg.decode()}`")

    # Recv Data From Server...
    server_msg, addr = client_socket_connection.recvfrom(MAX_BUFFER_SIZE)

    print(f"Received From `{SERVER_ADDR}`: Message => `{server_msg.decode()}`")

except error:
    print(error)
