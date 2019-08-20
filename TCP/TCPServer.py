import socket

host = "127.0.0.1"
port = 8000
buffer_size = 1024

TCP_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_server_socket.bind((host, port))
TCP_server_socket.listen(1)


def send_message(conn):
    while True:
        msg = conn.recv(buffer_size)
        if not msg:
            break

        conn.send(msg)

        print(f"Message from client: { msg } ")

    conn.close()


print("Server listening...")

while True:
    send_message(TCP_server_socket.accept()[0])
