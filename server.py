import socket


def main():
    HOST = "127.0.0.1"
    PORT = 23456
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((HOST, PORT))
    my_socket.listen()  # to start listening
    print(f"listening on {HOST} on port {PORT}")

    while True:
        conn, addr = my_socket.accept()  # accept the connection
        print(f"Connected by {addr}")
        data = conn.recv(1024)  # to get data

        conn.sendall(data.upper())  # to send data back


if __name__ == "__main__":
    main()
