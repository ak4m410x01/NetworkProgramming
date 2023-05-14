from socket import *
from struct import *

SERVER_MAX_CONNECTION = 5
SERVER_ADDR = ("127.0.0.1", 55555)


def recv_all():
    header_struct = Struct("!I")

    # Recv Msg Size
    msg_size = client_socket_connection.recv(header_struct.size)

    # unpack msg size (convert from bytes to integer)
    msg_size = header_struct.unpack(msg_size)

    # Send Msg Size
    client_msg = client_socket_connection.recv(msg_size[0])

    return client_msg


# Create Socket Connection
server_socket_connection = socket(AF_INET, SOCK_STREAM)

# Set sock option REUSEADDR = 1
server_socket_connection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind Socket with server addr
server_socket_connection.bind(SERVER_ADDR)

# Listing...
server_socket_connection.listen(SERVER_MAX_CONNECTION)

print(f"Listing at: `{SERVER_ADDR}`")

while True:
    try:
        print("=====================================")
        print("Waiting Client(s)...!!\n")

        # Accept Connection
        client_socket_connection, client_addr = server_socket_connection.accept()

        # Close Sending...
        client_socket_connection.shutdown(SHUT_WR)

        client_msg = ""

        while True:
            try:
                msg = recv_all()

                if not msg:
                    break

                client_msg += f"{msg.decode()}\n"

            except error:
                print(f"error while recving\nError:{error}")

        print(f"Received From {client_addr}:\n{client_msg}")

        # Close Connection
        client_socket_connection.close()

    except KeyboardInterrupt:
        print("***************************")
        print("   Connection Closed :(    ")
        print("***************************")

        # Close Server Socket Connection
        server_socket_connection.close()
        break

    except error:
        print(f"Client Connection Error:{error}")
