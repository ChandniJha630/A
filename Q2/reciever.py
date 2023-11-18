import socket

def receiver():
    host = '127.0.0.1'  # localhost
    port = 12345  # choose the same port as in sender.py

    # Create a socket object
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to a specific address and port
        receiver_socket.bind((host, port))

        # Listen for incoming connections
        receiver_socket.listen()

        print("Waiting for a connection...")

        # Accept a connection
        conn, addr = receiver_socket.accept()
        print(f"Connection established with {addr}")

        while True:
            # Receive data from the sender
            data = conn.recv(1024).decode()

            if not data:
                break

            print(f"Received message: {data}")

            if data.lower() == 'exit':
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection and the socket
        conn.close()
        receiver_socket.close()

if __name__ == "__main__":
    receiver()
