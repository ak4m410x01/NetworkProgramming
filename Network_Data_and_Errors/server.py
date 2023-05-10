import socket
import struct

SERVER_MAX_CONNECTION = 5
SERVER_ADDR = ("127.0.0.1", 55555)


def recv_all():
    header_struct = struct.Struct("!I")

    # Recv Msg Size
    msg_size = client_socket_connection.recv(header_struct.size)

    # Unpack msg size (convert from bytes into integer)
    msg_size = header_struct.unpack(msg_size)

    msg = client_socket_connection.recv(msg_size[0])

    return msg


# =========================================================================

# Create Socket Connection
server_socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set sock option REUSEADDR = 1
server_socket_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind Socket with server addr
server_socket_connection.bind(SERVER_ADDR)

# Listing...
server_socket_connection.listen(SERVER_MAX_CONNECTION)
print("===========================")
print(f"Listing at:{SERVER_ADDR}")
print("---------------------------")

# Accept Connection
client_socket_connection, client_addr = server_socket_connection.accept()

# Close Sending...
client_socket_connection.shutdown(socket.SHUT_WR)


client_msg = ""

while True:
    msg = recv_all()

    if not msg:
        break

    client_msg += f"{msg.decode()}\n"


print(f"{client_addr}:\n{client_msg}")

# Close Connection
client_socket_connection.close()
