import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()
port = 8000

# Bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# Set the maximum number of queued connections
server_socket.listen(2)

# Initialize the username and password
username1 = "user1"
password1 = "pass123"
username2 = "user2"
password2 = "pass456"

print('Waiting for clients to connect...')

# Accept incoming connections from clients
client1_socket, client1_address = server_socket.accept()
print('Client 1 connected:', client1_address)

client2_socket, client2_address = server_socket.accept()
print('Client 2 connected:', client2_address)

# Authenticate the clients
def authenticate_client(client_socket):
    username = client_socket.recv(1024).decode()
    password = client_socket.recv(1024).decode()
    if username == username1 and password == password1 or username == username2 and password == password2:
        client_socket.send('authenticated'.encode())
        return True
    else:
        client_socket.send('not authenticated'.encode())
        client_socket.close()
        return False

# Authenticate both clients
if authenticate_client(client1_socket) and authenticate_client(client2_socket):
    print('Both clients authenticated!')

# Communication loop
while True:
    # Client 1 sends message to client 2
    message = client1_socket.recv(1024).decode()
    client2_socket.send(message.encode())

    # Client 2 sends message to client 1
    message = client2_socket.recv(1024).decode()
    client1_socket.send(message.encode())


