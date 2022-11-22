import socket, sys

HOST = "127.0.0.1"
PORT = 12345

# AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for
# TCP, the protocol that will be used to transport messages in the network.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

s.bind((HOST, PORT))
