import socket

MAX_BUFFER_SIZE = 1024


def client_socket_udp(_server_ip: str, _server_port: int) -> None:
    # Create Socket
    _client_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Broadcast Option
    _client_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send Data to Server
    _client_msg = "Hi, Server".encode("ASCII")
    _server_addr = (_server_ip, _server_port)
    _client_connection_socket.sendto(_client_msg, _server_addr)

    # Recv Data from Server
    _server_msg, addr = _client_connection_socket.recvfrom(MAX_BUFFER_SIZE)

    print(f"{_server_addr} => {_server_msg.decode('ASCII')}")


server_ip = "<broadcast>"
server_port = 55555

client_socket_udp(server_ip, server_port)
