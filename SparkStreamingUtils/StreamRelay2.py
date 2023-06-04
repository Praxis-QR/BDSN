'''
This code was written by chatGPT using these two prompts

Restart from scratch. We need the code for a server written in python that continuously listens to a receiver TCP port and whenever it gets a message, it stores it in the queue. A client connects on second transmitter port and pulls out the messages from the queue. If there are no messages, then client gets nothing. However, if in the meantime, more messages arrive on the receiving port, the new messages are added to the queue so that the client can connect to the transmitter port and retrieve the same as well. 

please modify the code just generated so that the client socket is kept open as long as the server is running. should not be closed

'''


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
        message_queue.put(message)

# Thread function to handle transmitting messages to the client
def transmit_messages(transmitting_socket):
    client_socket, _ = transmitting_socket.accept()
    while True:
        if not message_queue.empty():
            message = message_queue.get()
            client_socket.send(message.encode())
            print("Transmitted ", message)

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

    # Start a thread to handle transmitting messages
    transmit_thread = threading.Thread(target=transmit_messages, args=(transmitting_socket,))
    transmit_thread.start()

    while True:
        pass  # Keep the server running

# Start the server
start_server()
