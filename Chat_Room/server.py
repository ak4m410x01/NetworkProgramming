from socket import *
from threading import *

MAX_BUFFER_SIZE = 1024
SERVER_MAX_CONNECTION = 5
SERVER_ADDR = ("127.0.0.1", 55555)

clients_db = []
names_db = []


def broadcast(msg) -> None:
    # Broadcast Message for all Users
    for client in clients_db:
        client.sendall(msg.encode("ASCII"))
        print(msg)

    return


def receive(connection) -> None:
    while True:
        try:
            # Recv Message From Client then Broadcast this message to all Clients
            client_msg = connection.recv(MAX_BUFFER_SIZE).decode("ASCII")
            broadcast(f"{client_name}=> {client_msg}")

        except error:
            print(error)

            connection.close()

            idx = clients_db.remove(connection)
            broadcast(f" ):  /{names_db[idx]}\\ Left from chat room  :( ")

            # Remove Client From DB
            clients_db.pop(idx)
            names_db.pop(idx)

            break


# Create Socket Connection
server_socket_connection = socket(AF_INET, SOCK_STREAM)

# Set Sock REUSEADDR option = 1
server_socket_connection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind Socket with Server Address
server_socket_connection.bind(SERVER_ADDR)

# Listing...
server_socket_connection.listen(SERVER_MAX_CONNECTION)

print(f"Listing at: `{SERVER_ADDR}`... :)")


while True:
    try:
        # Accept Socket Connection
        client_socket_connection, client_addr = server_socket_connection.accept()

        # Request Client Name
        client_socket_connection.sendall("name".encode("ASCII"))
        client_name = client_socket_connection.recv(MAX_BUFFER_SIZE).decode("ASCII")

        # add client name & client connection to db
        clients_db.append(client_socket_connection)
        names_db.append(client_name)

        # Broadcast "Join Message"
        broadcast(f" (:  /{client_name}\\ joined to chat room  :)")

        # Create Receive Thread and start it
        receive_thread = Thread(
            target=receive,
            args={
                client_socket_connection,
            },
        )

        receive_thread.start()

    except KeyboardInterrupt:
        print("***************************")
        print("   Connection Closed :(    ")
        print("***************************")

        client_socket_connection.close()

        break
