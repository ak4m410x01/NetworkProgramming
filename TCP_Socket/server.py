import socket

MAX_BUFFER_SIZE = 1024
MAX_SERVER_CONNECTION = 5
SERVER_ADDR = ("127.0.0.1", 55555)


def server_socket_tcp(server_addr: tuple) -> None:
    # Create Socket Connection
    server_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set Socket Option REUSEADDR = 1
    server_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind Socket with server addr
    server_connection_socket.bind(server_addr)

    # Listen...
    server_connection_socket.listen(MAX_SERVER_CONNECTION)

    print(f"Listing at:{server_addr}... :)")

    while True:
        try:
            print("=====================================")
            print("Waiting Client(s)...!!\n")

            # Accept Connection
            client_connection, _client_addr = server_connection_socket.accept()

            # Recv Data
            client_msg = client_connection.recv(MAX_BUFFER_SIZE)
            print(f"{_client_addr} => {client_msg.decode('ASCII')}")

            # Send Data
            server_msg = "Hi, Client :)".encode("ASCII")
            client_connection.sendall(server_msg)

            print(f"{server_addr} => {server_msg.decode('ASCII')}")

            # Close Connection
            client_connection.close()

        except KeyboardInterrupt:
            print("***************************")
            print("   Connection Closed :(    ")
            print("***************************")
            break


# Call Socket Method
# server_socket_tcp(SERVER_ADDR)
