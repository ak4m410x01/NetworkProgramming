import socket

MAX_BUFFER_SIZE = 1024


def server_socket_udp(_server_ip: str, _server_port: int) -> None:
    # Create Socket
    _server_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Broadcast Option
    _server_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Bind Socket with (serverIP,serverPort)
    _server_addr = (_server_ip, _server_port)
    _server_connection_socket.bind(_server_addr)

    while True:
        try:
            print("=====================================")
            print("\n Waiting...!!")

            # Recv Data from client(s)...
            _client_msg, _client_addr = _server_connection_socket.recvfrom(
                MAX_BUFFER_SIZE
            )

            print(f"{_client_addr} => {_client_msg.decode('ASCII')}")

            # Send Data to Client(s)
            _server_msg = "Hi, Client\n".encode("ASCII")
            _server_connection_socket.sendto(_server_msg, _client_addr)

            print(f"{_server_addr} => {_server_msg.decode('ASCII')}")

        except KeyboardInterrupt:
            print("***************************")
            print("   Connection Closed :(    ")
            print("***************************")
            break


server_ip = "<broadcast>"
server_port = 55555

server_socket_udp(server_ip, server_port)
