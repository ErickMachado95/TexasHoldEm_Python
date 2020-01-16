import socket
import threading
import buffer


HEADERSIZE = 8 

games = {}

game_lock = threading.Lock()



def server_control(client_socket,address):
    intro_msg = "Welcome to e-poker!"
    buffer.send_msg(client_socket,intro_msg)
    msg = buffer.recv_msg(client_socket)
    if msg == "HOST":
        host_setup(client_socket)
    else:
        join_setup(client_socket)

    client_socket.close()
    print(f"Connection from {address} closed")


def host_setup(socket):
    while True:
        game_name = buffer.recv_msg(socket)
        game_lock.acquire()
        if game_name in games:
            buffer.send_msg(socket,"FALSE")
            game_lock.release()
            continue
        else:
            games[game_name] = "BLAH"
            buffer.send_msg(socket,"TRUE")
            game_lock.release()
            break





def join_setup(socket):
    return
    
s = socket.socket()

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 

print(f"Host name is: {host_name}")
print(f"Host ip is : {host_ip}")

port = 1234
s.bind(('', port))
print(f"Port is: {port}")
s.listen(4)


while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established")
    thrd = threading.Thread(target=server_control,args=(client_socket,address,))
    thrd.start()


