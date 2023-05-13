from socket import *

MAX_BUFFER_SIZE = 1024


# Get Server addr info
server_info = getaddrinfo(
    None,
    55555,
    AF_INET,
    SOCK_STREAM,
)

try:
    # Create Socket Connection
    client_socket_connection = socket(*server_info[0][0:3])

    # Connect with server
    client_socket_connection.connect(server_info[0][4])

    # Send Data To Server...
    client_msg = "Hi, Server".encode()
    client_socket_connection.sendall(client_msg)

    print(f"Send To `{server_info[0][4]}: Message => {client_msg.decode()}`")

    # Recv Data From Server...
    server_msg = client_socket_connection.recv(MAX_BUFFER_SIZE)

    print(f"Received From `{server_info[0][4]}: Message => {server_msg.decode()}`")

    # Close Connection
    client_socket_connection.close()

except KeyboardInterrupt:
    print("***************************")
    print("   Connection Closed :(    ")
    print("***************************")

except error:
    print(error)
