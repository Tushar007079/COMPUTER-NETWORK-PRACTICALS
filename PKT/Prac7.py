import socket

def chat_server(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)  # Listen for incoming connections

    print("Server is waiting for a connection...")
    client_socket, client_addr = server_socket.accept()
    print(f"Connected to {client_addr}")

    while True:
        message = input("Server: ")
        client_socket.send(message.encode())

        received_message = client_socket.recv(1024).decode()
        print(f"Client: {received_message}")

        if "work is done" in received_message.lower():
            break

    server_socket.close()
    client_socket.close()

def chat_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        message = input("Client: ")
        client_socket.send(message.encode())

        received_message = client_socket.recv(1024).decode()
        print(f"Server: {received_message}")

        if "work is done" in received_message.lower():
            break

    client_socket.close()

def main():
    role = input("Enter 'server' or 'client': ")
    server_ip = '172.31.112.1'
    server_port = 1077

    if role.lower() == 'server':
        chat_server(server_ip, server_port)
    elif role.lower() == 'client':
        chat_client(server_ip, server_port)
    else:
        print("Invalid role. Please enter 'server' or 'client'.")

if __name__ == "__main__":
    main()
