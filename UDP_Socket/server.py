from socket import *

SERVER_ADDR = ('127.0.0.1', 55555)
MAX_BUFFER_SIZE = 1024

# Create Socket Connection
server_socket_connection = socket(AF_INET, SOCK_DGRAM)

# Bind Socket with server address
server_socket_connection.bind(SERVER_ADDR)

while True:
    try:
        print("=====================================")
        print("Waiting Client(s)...!!\n")

        # Recv Data From Client(s)...
        client_msg, client_addr = server_socket_connection.recvfrom(MAX_BUFFER_SIZE)

        print(f"Received From `{client_addr}`: Message => `{client_msg.decode()}`")

        # Send Data to Client(s)...
        server_msg = "Hi, Client... :)".encode()
        server_socket_connection.sendto(server_msg, client_addr)

        print(f"Send To `{client_addr}`: Message `{server_msg.decode()}`")

    except KeyboardInterrupt:
        print("***************************")
        print("   Connection Closed :(    ")
        print("***************************")

        break

    except error:
        print(error)
