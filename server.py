import socket
import threading
import comm
import game
import time


HEADERSIZE = 8 

games = {}

game_lock = threading.Lock()



def server_control(client_socket,address):
    intro_msg = "Welcome to e-poker!"
    comm.send_msg(client_socket,intro_msg)
    msg = comm.recv_msg(client_socket)
    game_setup = False
    if msg == "HOST":
        game_setup = host_setup(client_socket)
    else:
        join_setup(client_socket)
    if not game_setup:
        client_socket.close()
        print(f"Connection from {address} closed")
    else:
        print(f"Game Established")

def run_game(game_name,expected_players):
    game_lock.acquire()
    running_game = games[game_name]
    game_lock.release()
    current_num_players = len(running_game.list_of_player_names())
    old_num_players = current_num_players
    while True: 
        current_num_players = len(running_game.list_of_player_names())
        if current_num_players != old_num_players:
            wait_players = expected_players - current_num_players
            for player in running_game.list_of_players():
                comm.send_msg(player.socket,"MSG")
                comm.send_msg(player.socket,f"Waiting, on {wait_players} player(s)")

        old_num_players = current_num_players
        if current_num_players == expected_players: 
            for player in running_game.list_of_players():
                comm.send_msg(player.socket,f"Game, beginning")
            break
        time.sleep(2)




def host_setup(socket):
    while True:
        game_name = comm.recv_msg(socket)
        if game_name:
            game_lock.acquire()
            if game_name in games:
                comm.send_msg(socket,"FALSE")
                game_lock.release()
                continue
            else:
                games[game_name] = game.Game(game_name,0)
                comm.send_msg(socket,"TRUE")
                while True:
                    num_players = comm.recv_msg(socket)
                    if num_players:
                            comm.send_msg(socket,"TRUE")
                            while True:
                                player_name = comm.recv_msg(socket)
                                if player_name:
                                    if player_name in games[game_name].list_of_player_names():
                                        comm.send_msg(socket,"FALSE")
                                        continue
                                    else:
                                        games[game_name].add_player(socket,player_name)
                                        comm.send_msg(socket,"TRUE")
                                        response = comm.recv_msg(socket)
                                        if response:
                                            if response == "TRUE":
                                                rg = threading.Thread(target=run_game, args=(game_name, num_players,))
                                                rg.start()
                                            else:
                                                game_lock.release()
                                                return False
                                        game_lock.release()
                                        return True
                                else:
                                    game_lock.release()
                                    return False

                    else:
                        game_lock.release()
                        return False
        else:
            return False







def join_setup(socket):
    while True:
        game_name = comm.recv_msg(socket)
        if game_name:
            game_lock.acquire()
            if game_name in games:
                comm.send_msg(socket,"TRUE")
                while True:
                    player_name = comm.recv_msg(socket)
                    if player_name:
                        if player_name in games[game_name].list_of_player_names():
                            comm.send_msg(socket,"FALSE")
                        else:
                            comm.send_msg(socket,"TRUE")
                            games[game_name].add_player(socket,player_name)
                            game_lock.release()
                            return True
                    else:
                        game_lock.release()
                        return False
            else:
                game_lock.release()
                continue

        else:
            return False

    
s = socket.socket()

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 

print(f"Host name is: {host_name}")
print(f"Host ip is : {host_ip}")

port = 1241
s.bind(('', port))
print(f"Port is: {port}")
s.listen(4)


while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established")
    thrd = threading.Thread(target=server_control,args=(client_socket,address,))
    thrd.start()


