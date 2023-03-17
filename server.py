import socket

def handle_request(conn):
    data = conn.recv(1024)
    if not data:
        return
    try:
        a, b = map(int, data.decode().strip().split("+"))
        result = a + b
        conn.sendall(str(result).encode())
    except ValueError:
        conn.sendall(b"Invalid request format")

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 8000))
        s.listen()
        print("Server is listening on port 8000...")
        while True:
            conn, addr = s.accept()
            print(f"New client connected: {addr}")
            handle_request(conn)
            conn.close()

if __name__ == "__main__":
    run_server()
