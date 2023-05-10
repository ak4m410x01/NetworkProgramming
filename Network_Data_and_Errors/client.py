import socket
import struct

SERVER_ADDR = ("127.0.0.1", 55555)


def send_all(msg: str):
    header_struct = struct.Struct("!I")

    msg_size = len(msg)

    # Send Message Size
    client_socket_connection.sendall(header_struct.pack(msg_size))

    # Send Main Message
    client_socket_connection.sendall(msg.encode())


# =========================================================================

# Create Socket Connection
client_socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect with server
client_socket_connection.connect(SERVER_ADDR)


send_all("Hello, Server")
send_all("Hi, server")
send_all("Welcome Server")
send_all("")

# Close Connection
client_socket_connection.close()
