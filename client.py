import socket 

def main():
    HOST = '127.0.0.1'
    PORT = 23456
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((HOST, PORT))
    my_massage = input("Enter your massage\n")
    my_socket.sendall(bytes(my_massage, 'utf-8'))
    data = my_socket.recv(1024) # to gat data
    print(f"Received back", data)

if __name__ =="__main__":
    main()