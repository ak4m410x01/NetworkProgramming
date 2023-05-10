import socket

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("127.0.0.1", 55555)


def client_socket_tcp(server_addr: tuple):
    # Create Socket Connection
    client_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect with server
    client_connection_socket.connect(server_addr)

    # Send Data
    client_msg = "Hi, Server".encode("ASCII")
    client_connection_socket.sendall(client_msg)

    # Recv Data
    server_msg = client_connection_socket.recv(MAX_BUFFER_SIZE)

    print(f"{server_addr} => {server_msg}")

    # Close
    client_connection_socket.close()


# Call Socket Method
# client_socket_tcp(SERVER_ADDR)
