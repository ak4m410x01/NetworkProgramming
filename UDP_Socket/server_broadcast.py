import socket

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("0.0.0.0", 55555)


def server_socket_udp(server_addr: tuple) -> None:
    # Create Socket Connection
    server_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set Sock Option SO_BROADCAST = 1
    server_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Bind Socket with server_addr
    server_connection_socket.bind(server_addr)

    while True:
        try:
            print("=====================================")
            print("Waiting Client(s)...!!\n")

            # Recv Data from client(s)...
            client_msg, client_addr = server_connection_socket.recvfrom(MAX_BUFFER_SIZE)

            print(f"{client_addr} => {client_msg.decode('ASCII')}")

            # Send Data to Client(s)
            server_msg = "Hi, Client\n".encode("ASCII")
            server_connection_socket.sendto(server_msg, client_addr)

            print(f"{server_addr} => {server_msg.decode('ASCII')}")

        except KeyboardInterrupt:
            print("***************************")
            print("   Connection Closed :(    ")
            print("***************************")
            break


# Call Socket Method
# server_socket_udp(SERVER_ADDR)
