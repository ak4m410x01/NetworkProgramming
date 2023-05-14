from socket import *
from struct import *

SERVER_ADDR = ("127.0.0.1", 55555)


def send_all(msg: str) -> None:
    header_struct = Struct("!I")

    msg_size = len(msg)

    # Send Message Size
    client_socket_connection.sendall(header_struct.pack(msg_size))

    # Send Main Message
    client_socket_connection.sendall(msg.encode())


# Create Socket Connection
client_socket_connection = socket(AF_INET, SOCK_STREAM)

# Connect with server
client_socket_connection.connect(SERVER_ADDR)

# Close Recv option
client_socket_connection.shutdown(SHUT_RD)

send_all("Hello, Server")
send_all("Hi, server")
send_all("Welcome Server")
send_all("")

# Close Connection
client_socket_connection.close()
