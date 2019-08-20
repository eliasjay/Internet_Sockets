import socket

server_address = ("127.0.0.1", 8000)
buffer_size = 1024

UDP_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter message: ")
    bytes_to_send = str.encode(message)

    UDP_client_socket.sendto(bytes_to_send, server_address)
    bytes_pair = UDP_client_socket.recvfrom(buffer_size)

    server_msg = bytes_pair
    print(f"Message to Server { server_msg }")
