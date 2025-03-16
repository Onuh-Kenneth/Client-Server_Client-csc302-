import socket

# Server configuration
HOST = '127.0.0.1'  # Server address (localhost)
PORT = 12345         # Port to connect to

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Connect to server

message = client_socket.recv(1024).decode()  # Receive message from server
print(f"Server says: {message}")

client_socket.close()  # Close connection
