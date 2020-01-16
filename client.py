import socket
import threading
import comm



HEADERSIZE = 8


def host(socket):
    game_name = input("Input name of your game")
    comm.send_msg(socket,game_name)

    while True:
        game_est = comm.recv_msg(socket);
        if game_est == "TRUE":
            print(f"Game {game_name} has been established")
            while True:
                try:
                    player_cnt = int(input("Enter player count (MAX 4): "))
                    if 0 < player_cnt < 5:
                        comm.send_msg(socket,str(player_cnt))
                        player_name = input("Enter player name: ")
                        comm.send_msg(socket,player_name)
                        break
                    else:
                        print("Wrong number of players")
                except:
                    print("Wrong input")

        elif game_est == "FALSE":
            print(f"Sorry game {game_name} already exists")
            game_name = input("Type in other game name: ")
            comm.send_msg(socket, game_name)
        else:
            return




def join(socket):
    return


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Type Host IP: ")
port = int(input("Type Port: "))

s.connect((ip,port))

msg = comm.recv_msg(s)

print(msg)

pref = ''
while True:
    try:
        pref = int(input("Would you like to Host (0)  or Join (1)  a game? (Please Type in Number)"))
        if pref == 0:
            comm.send_msg(s,"HOST")
            host(s)
            break
        elif pref == 1:
            comm.send_msg(s,"JOIN")
            join(s)
            break
        else:
            print("Wrong input, Please try again")
    except:
        print("Wrong input, Please try again")



print("Disconnected from server")
exit(0)
