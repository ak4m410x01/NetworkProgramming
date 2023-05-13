from socket import *

SERVER_MAX_CONNECTION = 5
MAX_BUFFER_SIZE = 1024


# Get Server addr info
server_info = getaddrinfo(
    None,
    55555,
    AF_INET,
    SOCK_STREAM,
)

# Create Socket Connection
server_socket_connection = socket(*server_info[0][0:3])

# Bind Socket with server addr
server_socket_connection.bind(server_info[0][4])

# Listing...
server_socket_connection.listen(SERVER_MAX_CONNECTION)

print(f"Listing at: `{server_info[0][4]}`")

while True:
    try:
        print("=====================================")
        print("Waiting Client(s)...!!\n")

        # Accept Connection(s)...
        client_socket_connection, client_addr = server_socket_connection.accept()

        # Recv Data From Client...
        client_msg = client_socket_connection.recv(MAX_BUFFER_SIZE)

        print(f"Received From `{client_addr}: Message => {client_msg.decode()}`")

        # Send Data To Client...
        server_msg = "Hi, Client".encode()
        client_socket_connection.sendall(server_msg)

        print(f"Send To `{client_addr}: Message => {server_msg.decode()}`")

        # Close Connection
        client_socket_connection.close()

    except KeyboardInterrupt:
        print("***************************")
        print("   Connection Closed :(    ")
        print("***************************")

        break

    except error:
        print(error)
