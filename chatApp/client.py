import socket
import threading

# Global variables
HOST = '127.0.0.1'  # Localhost
PORT = 12345         # Port for communication

def receive_messages(client_socket):
    """Receives messages from the server."""
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(f"Error receiving message from server: {str(e)}")
            break

def send_messages(client_socket):
    """Sends messages to the server."""
    while True:
        try:
            # Input message from user
            message = input("Enter your message: ")
            if message:
                # Send message to server
                client_socket.sendall(message.encode('utf-8'))
            else:
                print("Message cannot be empty.")
        except Exception as e:
            print(f"Error sending message to server: {str(e)}")
            break

def start_client():
    """Starts the client to connect to the server."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect client to server
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Connected to server on {HOST}:{PORT}")

        # Start threads for sending and receiving messages
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        send_thread = threading.Thread(target=send_messages, args=(client,))
        
        receive_thread.start()
        send_thread.start()

    except Exception as e:
        print(f"Error connecting to server: {str(e)}")
        client.close()

if __name__ == "__main__":
    start_client()


