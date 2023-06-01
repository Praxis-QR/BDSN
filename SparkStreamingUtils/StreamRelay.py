import socket
import threading
import queue

# Create a queue to store incoming messages
message_queue = queue.Queue()

# Thread function to handle incoming messages and add them to the queue
def handle_messages(receiving_socket):
    while True:
        client_socket, _ = receiving_socket.accept()
        message = client_socket.recv(1024).decode()
        print('received ',message)
        message_queue.put(message)
        client_socket.close()

# Function to start the server
def start_server():
    # Create a socket for receiving messages
    receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiving_socket.bind(('localhost', 8000))
    receiving_socket.listen(1)
    print("Server started. Listening for incoming messages on port 8000.")

    # Create a socket for transmitting messages
    transmitting_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transmitting_socket.bind(('localhost', 9000))
    transmitting_socket.listen(1)
    print("Transmitting messages to clients on port 9000.")

    # Start a thread to handle incoming messages
    message_thread = threading.Thread(target=handle_messages, args=(receiving_socket,))
    message_thread.start()

    while True:
        # Accept a client connection on the transmitting socket
        client_socket, _ = transmitting_socket.accept()
        messages = []

        # Check if there are any messages in the queue
        while not message_queue.empty():
            message = message_queue.get()
            messages.append(message)

        # Send the messages to the client
        if messages:
            client_socket.send('\n'.join(messages).encode())
            print('sent ',message)

        client_socket.close()

# Start the server
start_server()