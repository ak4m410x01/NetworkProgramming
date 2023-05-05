import socket
import threading

MAX_CONNECTION = 5
MAX_BUFFER_SIZE = 1024
clients_db = []


def connection_close() -> None:
    print("***************************")
    print("   Connection Closed :(    ")
    print("***************************")


def broadcast(_msg: str) -> None:
    for client in clients_db:
        print(_msg)
        client["connection"].sendall(_msg.encode("ASCII"))

    return


def receive() -> None:
    while True:
        try:
            # Recv Messages and Broadcast
            _client_msg = f"{_client_name}: {_client_connection_socket.recv(MAX_BUFFER_SIZE)}".decode(
                "ASCII"
            )
            broadcast(_client_msg)

        except:
            broadcast(f" ):  /{_client_name}\\ left chat room  :( ")

            clients_db.remove(
                {
                    "name": _client_name,
                    "connection": _client_connection_socket,
                },
            )

            _client_connection_socket.close()

            break

    return


server_ip = socket.gethostbyname(socket.gethostname())
server_port = 55555

# Create TCP Socket Connection
_server_connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set socket opt REUSEADDR = 1
_server_connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket with server addr
_server_addr = (server_ip, server_port)
_server_connection_socket.bind(_server_addr)

# Listen...
_server_connection_socket.listen(MAX_CONNECTION)

print(f"Listing at:{_server_addr}")

while True:
    try:
        print("=====================================")

        # Accept Client(s) connection...
        _client_connection_socket, _client_addr = _server_connection_socket.accept()

        # Request Client Name:
        _client_connection_socket.send("Name:".encode("ASCII"))
        _client_name = _client_connection_socket.recv(MAX_BUFFER_SIZE).decode("ASCII")

        # Add Client [Name, Connection] to DB
        clients_db.append(
            {
                "name": _client_name,
                "connection": _client_connection_socket,
            },
        )

        # join message broadcast...
        broadcast(f" (:  /{_client_name}\\ joined to chat room  :)")

        # recv func thread...
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

    except KeyboardInterrupt:
        connection_close()

        _server_connection_socket.close()

        break
