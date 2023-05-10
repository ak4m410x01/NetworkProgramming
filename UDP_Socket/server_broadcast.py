import socket

MAX_BUFFER_SIZE = 1024
SERVER_ADDR = ("0.0.0.0", 55555)


# Create Socket Connection
server_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set Sock Option SO_BROADCAST = 1
server_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Bind Socket with SERVER_ADDR
server_connection_socket.bind(SERVER_ADDR)

while True:
    try:
        print("=====================================")
        print("Waiting Client(s)...!!\n")

        # Recv Data from client(s)...
        client_msg, client_addr = server_connection_socket.recvfrom(MAX_BUFFER_SIZE)

        print(f"{client_addr} => {client_msg.decode('ASCII')}")

        # Send Data to Client(s)
        server_msg = "Hi, Client\n".encode("ASCII")
        server_connection_socket.sendto(server_msg, client_addr)

        print(f"{SERVER_ADDR} => {server_msg.decode('ASCII')}")

    except KeyboardInterrupt:
        print("***************************")
        print("   Connection Closed :(    ")
        print("***************************")
        break
