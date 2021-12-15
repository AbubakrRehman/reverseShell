import socket
import sys


port=4000
host=""
s=socket.socket()

conn_list=[]
addr_list=[]

def send_command(conn):
    while True:
        cmd=input()
        if(cmd=='quit'):
            conn.close()
            s.close()
            sys.exit()
        if(len(cmd.encode('utf-8'))>0):
            try:
                conn.send(cmd.encode('utf-8'))
            except:
                print('Client got disconnected')
                print('waiting for client to connect.........')
                conn,addr=s.accept()
                print(f'Connection has been established! |IP {addr[0]} |PORT {addr[1]}')
                send_command(conn)
            client_response=conn.recv(4096).decode('utf-8')
            print(client_response,end="")

def create_server():
    try:
        port=4000
        host=""
        s=socket.socket()
    except socket.error as msg:
        print("Socket creation error: "+str(msg))

def bind_socket():
    try:
        print(f'binding the port {str(port)}')
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print(f'Socket binding error {str(msg)} \n Retrying')
        bind_socket()

def socket_accept():
    conn,addr=s.accept()
    print(conn)
    print(f'Connection has been established! |IP {addr[0]} |PORT {addr[1]}')
    send_command(conn)
    conn.close()

# def socket_accept_new():
#     while True:
#         conn,addr=s.accept()
#         conn_list.append(conn)
#         addr_list.append(addr)


if __name__=='__main__':
    create_server()
    bind_socket()
    socket_accept()
from array import _UnicodeTypeCode

    

        



