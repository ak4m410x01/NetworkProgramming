import socket

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("0.0.0.0", 55555)


def client_socket_udp(server_addr: tuple) -> None:
    # Create Socket Connection
    client_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set Sock Option SO_BROADCAST = 1
    client_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send Data to Server
    client_msg = "Hi, Server".encode("ASCII")
    client_connection_socket.sendto(client_msg, SERVER_ADDR)

    # Recv Data from Server

    server_msg, addr = client_connection_socket.recvfrom(MAX_BUFFER_SIZE)

    print(f"{server_addr} => {server_msg.decode('ASCII')}")


# Call Socket Method
# client_socket_udp(SERVER_ADDR)
