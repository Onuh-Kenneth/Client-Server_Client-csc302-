import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Port to listen on

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Listen for 1 client at a time

print(f"Server listening on {HOST}:{PORT}...")

while True:
    client_socket, client_address = server_socket.accept()  # Accept connection
    print(f"Connected by {client_address}")

    message = "Hello from the server!"
    client_socket.sendall(message.encode())  # Send message to client

    client_socket.close()  # Close connection
