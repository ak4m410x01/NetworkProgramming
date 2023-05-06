import socket

MAX_CONNECTION = 5

MAX_BUFFER_SIZE = 1023


# Get Info
_server_connection = socket.getaddrinfo(
    None,
    55555,
    socket.AF_INET,
    socket.SOCK_STREAM,
)


# Create Socket Connection
_server_connection_socket = socket.socket(*_server_connection[0][0:3])

# Bind socket with server addr
_server_addr = _server_connection[0][4]

_server_connection_socket.bind(_server_addr)

# Listing...
_server_connection_socket.listen(MAX_CONNECTION)

print(f"Listing at:{_server_addr}...")

while True:
    try:
        print("=====================================")
        print("\n Waiting...!!")

        # Accept Connection
        _client_connection_socket, _client_addr = _server_connection_socket.accept()

        # Recv Data...
        _client_msg = _client_connection_socket.recv(MAX_BUFFER_SIZE).decode("ASCII")

        print(f"{_client_addr}=> {_client_msg}")

        # Send Data...
        _server_msg = "Hi, Client".encode("ASCII")

        _client_connection_socket.sendall(_server_msg)

        # Close Connection
        _client_connection_socket.close()
    except KeyboardInterrupt:
        print("***************************")
        print("   Connection Closed :(    ")
        print("***************************")
        _server_connection_socket.close()
        break
