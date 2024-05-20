import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()
port = 8000

# Connect to the server
client_socket.connect((host, port))

# Authenticate with the server
username = input('Username: ')
password = input('Password: ')
client_socket.send(username.encode())
client_socket.send(password.encode())
response = client_socket.recv(1024).decode()

if response == 'authenticated':
    print('Authenticated!')
else:
    print('Not authenticated!')

# Communication loop
while True:
    # Client 2 receives message from client 1
    message = client_socket.recv(1024).decode()
    print("Received from client 1:", message)

    # Client 2 sends message to client 1
    message = input("Client 2: ")
    client_socket.send(message.encode())
    if message == "exit":
        exit()

client_socket.close()
