import socket

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("0.0.0.0", 55555)


# Create Socket Connection
client_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send Data to Server
client_msg = "Hi, Server".encode("ASCII")
client_connection_socket.sendto(client_msg, SERVER_ADDR)

# Recv Data from Server

_server_msg, addr = client_connection_socket.recvfrom(MAX_BUFFER_SIZE)

print(f"{SERVER_ADDR} => {_server_msg.decode('ASCII')}")
