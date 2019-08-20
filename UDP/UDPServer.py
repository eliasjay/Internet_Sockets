import socket

host = "127.0.0.1"
port = 8000
buffer_size = 1024

UDP_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_server_socket.bind((host, port))

print("Server listening...")

while True:
    bytes_pair = UDP_server_socket.recvfrom(buffer_size)
    client_msg = bytes_pair[0]
    client_address = bytes_pair[1]

    print(f"Message from client: { client_msg }")

    UDP_server_socket.sendto(client_msg, client_address)
