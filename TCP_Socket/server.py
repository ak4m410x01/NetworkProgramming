import socket

MAX_BUFFER_SIZE = 1024


def server_socket_tcp(_server_ip: str, _server_port: int) -> None:
    # Create Socket
    _server_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set Option REUSEADDR = 1
    _server_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind Socket
    _server_addr = (_server_ip, _server_port)
    _server_connection_socket.bind(_server_addr)

    # Listen
    MAX_CONNECTION = 5
    _server_connection_socket.listen(MAX_CONNECTION)
    print(f"Listing at:{_server_addr}")
    while True:
        try:
            print("=====================================")
            print("\n Waiting...!!")

            # Accept Connection
            _client_connection, _client_addr = _server_connection_socket.accept()

            # Recv Data
            _client_msg = _client_connection.recv(MAX_BUFFER_SIZE)
            print(f"{_client_addr} => {_client_msg.decode('ASCII')}")

            # Send Data
            _server_msg = "Hi, Client :)".encode("ASCII")
            _client_connection.sendall(_server_msg)

            print(f"{_server_addr} => {_server_msg.decode('ASCII')}")

            # Close Connection
            _client_connection.close()

        except KeyboardInterrupt:
            print("***************************")
            print("   Connection Closed :(    ")
            print("***************************")
            break


server_ip = socket.gethostbyname(socket.gethostname())
server_port = 55555

server_socket_tcp(server_ip, server_port)
