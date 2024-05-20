# Client-Server Chat Application Using Sockets

This project implements a simple client-server chat application using Python sockets. The server can handle two clients, authenticating them based on predefined usernames and passwords, and facilitating message exchange between them.

## Features

- **Client-Server Architecture**: The server handles connections and authentication for two clients.
- **Authentication**: Clients must provide a correct username and password to communicate.
- **Message Exchange**: Authenticated clients can send messages to each other through the server.
- **Exit Mechanism**: Clients can exit the chat by typing "exit".

## Requirements

- Python 3.x
- Local network or a common network to connect the server and clients

## Files

- `server.py`: The server-side code.
- `client1.py`: The code for the first client.
- `client2.py`: The code for the second client.

## Setup

1. **Ensure all devices are on the same network**: The server and clients should be able to communicate over the same network.

2. **Run the Server**:
   - Save the server-side code in a file named `server.py`.
   - Execute the server script:
     ```sh
     python server.py
     ```

3. **Run the Clients**:
   - Save the first client-side code in a file named `client1.py`.
   - Save the second client-side code in a file named `client2.py`.
   - Execute the client scripts on separate terminals or different machines:
     ```sh
     python client1.py
     ```
     ```sh
     python client2.py
     ```

## Usage

1. **Start the Server**: Run the `server.py` script on the server machine.
2. **Connect Clients**: Run the `client1.py` and `client2.py` scripts on two separate client machines.
3. **Authenticate**: Enter the username and password on both clients. 
4. **Chat**: Once authenticated, clients can send and receive messages through the server. Type "exit" to leave the chat.

## Notes

- Ensure the server is running before starting the clients.
- The server is currently configured to handle exactly two clients. To handle more clients, you would need to implement a more complex server with threading or asynchronous I/O.
- The provided usernames and passwords are hard-coded for simplicity. For a real application, consider a secure authentication mechanism.

