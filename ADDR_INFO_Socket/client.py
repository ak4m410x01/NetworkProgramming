import socket


MAX_BUFFER_SIZE = 1023


# Get Info
_client_connection = socket.getaddrinfo(
    None,
    55555,
    socket.AF_INET,
    socket.SOCK_STREAM,
)

# Create Socket Connection
_client_connection_socket = socket.socket(*_client_connection[0][0:3])

try:
    # Connect with server
    _server_addr = _client_connection[0][4]

    _client_connection_socket.connect(_server_addr)

    # Send Data...
    _client_msg = "Hi, Server".encode("ASCII")

    _client_connection_socket.sendall(_client_msg)

    # Recv Data...
    _server_msg = _client_connection_socket.recv(MAX_BUFFER_SIZE).decode("ASCII")

    print(f"{_server_addr}=> {_server_msg}")
except KeyboardInterrupt:
    print("***************************")
    print("   Connection Closed :(    ")
    print("***************************")

_client_connection_socket.close()
