import socket

MAX_BUFFER_SIZE = 1024


def client_socket_tcp(_server_ip, _server_port):
    # Create Socket
    _client_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect
    _server_addr = (_server_ip, _server_port)
    _client_connection_socket.connect(_server_addr)

    # Send
    _client_msg = "Hi, Server".encode("ASCII")
    _client_connection_socket.sendall(_client_msg)

    # Recv
    _server_msg = _client_connection_socket.recv(MAX_BUFFER_SIZE)

    print(f"{_server_addr} => {_server_msg}")

    # Close
    _client_connection_socket.close()


server_ip = socket.gethostbyname(socket.gethostname())
server_port = 55555

client_socket_tcp(server_ip, server_port)
