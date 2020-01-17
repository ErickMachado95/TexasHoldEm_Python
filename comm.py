import socket 
import threading


HEADERSIZE = 8 


def recv_msg(socket): 
    try:
        full_msg = ''
        msg = socket.recv(8)
        msglen = int(msg[:HEADERSIZE])
        while True:
            msg = socket.recv(16)
            full_msg +=msg.decode("utf-8")

            if len(full_msg) == msglen:
                return full_msg
    except:
        return ''


def send_msg(socket,msg):
    msg = f'{len(msg):<{HEADERSIZE}}'+msg
    socket.send(bytes(msg,"utf-8"))

