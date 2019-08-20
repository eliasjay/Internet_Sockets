import socket

host = "127.0.0.1"
port = 8000
buffer_size = 1024

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((host, port))

while True:
    message = input("Enter message: ")
    tcp.send(message.encode())
    message = tcp.recv(buffer_size)
    if not message:
        break
    print(f"Message to server { message }")

tcp.close()
