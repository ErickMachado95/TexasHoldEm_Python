import socket
import threading
import comm



HEADERSIZE = 8

def playing(socket):
    while True: 
        msg = comm.recv_msg(socket)
        if msg:
            if msg == "MSG":
                msg = comm.recv_msg(socket)
                print(msg)
            elif msg == "TABLE":
                print("TABLE")
            else:
                print(f"ERROR, in SERVER MESSAGE. MESSAGE IS {msg} EXPECTED MSG OR TABLE")
        else:
            break 



def game_name_host(socket):
    game_name = input("Input name of your game: ")
    comm.send_msg(socket,game_name)
    while True:
        game_est = comm.recv_msg(socket)
        if game_est:
            if game_est == "TRUE":
                print(f"Game {game_name} has been established")
                return True
            elif game_est == "FALSE":
                print(f"Sorry game {game_name} already exists")
                game_name = input("Enter other game name: ")
                comm.send_msg(socket, game_name)
                continue
            else:
                print("ERROR IN TRANSMISSION")
                return False
        else: 
            return False


def game_name_join(socket):
    game_name = input("Input name of the game to join: ")
    comm.send_msg(socket,game_name)
    while True:
        game_est = comm.recv_msg(socket)
        if game_est:
            if game_est == "TRUE":
                print("Joined game")
                return True
            elif game_est == "FALSE":
                print("Game \"{game_name}\" does not exist")
                game_name = input("Input other game name: ")
                comm.send_msg(socket,game_name)
                continue
            else:
                print("ERROR IN TRANSMISSION")
                return False
        else:
            return False

def player_name(socket):
    player_name = input("Enter player name: ")
    comm.send_msg(socket,player_name)
    while True:
        player_added = comm.recv_msg(socket)
        if player_added:
            if player_added == "TRUE":
                print(f"Player \"{player_name}\" added to game")
                return True
            elif player_added == "FALSE":
                print(f"Player \"{player_name}\" already exists")
                player_name = input("Enter other player name: ")
                comm.send_msg(socket,player_name)
                continue
            else:
                print("ERROR IN TRANSMISSION")
                return False
        else:
            return False
def num_players(socket):
    while True:
        try: 
            num = int(input("Enter the number of players (2-4): "))
            if 1 < num < 5: 
                comm.send_msg(socket,str(num))
                return True
            else: 
                print("Invalid number of players")
        except:
            print("Invalid input")
    

def host(socket):
    try:
        if game_name_host(socket):
            if num_players(socket):
                if player_name(socket):
                    print("waiting for players...")
                    playing(socket) 
 
    except Exception as e:
        print(f"Error occurred due to exception: {e}")


def join(socket):
    try:
        if game_name_join(socket):
            if player_name(socket):
                playing(socket)

    except Exception as e:
        print(f"Error occurred ude to exception: {e}")
        

       


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Type Host IP: ")
port = int(input("Type Port: "))

s.connect((ip,port))

msg = comm.recv_msg(s)

print(msg)

pref = ''
while True:
    try:
        pref = int(input("Would you like to Host (0)  or Join (1)  a game? (Please Type in Number) "))
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
