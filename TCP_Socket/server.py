from socket import *

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("127.0.0.1", 55555)
SERVER_MAX_CONNECTION = 5

# Create Socket Connection
server_socket_connection = socket(AF_INET, SOCK_STREAM)

# Set Sock REUSEADDR option = 1
server_socket_connection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind Socket with Server addr
server_socket_connection.bind(SERVER_ADDR)

# Listing...
server_socket_connection.listen(SERVER_MAX_CONNECTION)

print(f"Listing at: `{SERVER_ADDR}`")

while True:
    try:
        print("=====================================")
        print("Waiting Client(s)...!!\n")

        # Accept Socket Connection
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
