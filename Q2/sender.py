import socket

def sender():
    host = '127.0.0.1'  # localhost
    port = 12345  # choose a port

    # Create a socket object
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the receiver
        sender_socket.connect((host, port))
        print("Connection established with the receiver.")

        while True:
            # Get user input for the message
            message = input("Enter your message (type 'exit' to close): ")

            # Send the message
            sender_socket.sendall(message.encode())

            if message.lower() == 'exit':
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        sender_socket.close()

if __name__ == "__main__":
    sender()
