import socket 
import sys

def run_server():
    def interact(conn):
        while True:
            cmd = input(">")
            if cmd == 'exit':
                conn.close()
                s.close()
                sys.exit()
            if len(cmd) > 0:
                conn.send(cmd.encode())
                resp = conn.recv(2048)
                print(resp.decode())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 4444))
    s.listen(1)
    print("listening")
    conn, addr = s.accept()
    print("Connection established")


    while True:
        interact(conn)
if __name__ == "__main__":
    run_server()