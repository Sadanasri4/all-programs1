import socket
import threading

# Global variables
HOST = '127.0.0.1'  # Localhost
PORT = 12345         # Port for communication
clients = []         # List to keep track of connected clients

def handle_client(client_socket, client_address):
    """Handles messages from a single client."""
    print(f"[NEW CONNECTION] {client_address} connected.")

    # Add client to the list
    clients.append(client_socket)

    # Continuous message handling
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{client_address}] {message}")

                # Broadcast message to all clients except sender
                broadcast(message, client_socket)
            else:
                # If message is empty, client disconnected
                remove_client(client_socket)
                break
        except Exception as e:
            print(f"Error handling client {client_address}: {str(e)}")
            remove_client(client_socket)
            break

def broadcast(message, sender_client):
    """Broadcasts a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_client:
            try:
                client.sendall(message.encode('utf-8'))
            except:
                # Remove broken client connections
                remove_client(client)

def remove_client(client_socket):
    """Removes a client from the list and closes their connection."""
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    """Starts the server to listen for incoming connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind server to the specified host and port
        server.bind((HOST, PORT))
    except socket.error as e:
        print(str(e))

    # Listen for incoming connections
    server.listen()

    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    # Handle incoming connections
    while True:
        # Accept a client connection
        client_socket, client_address = server.accept()

        # Create a thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
