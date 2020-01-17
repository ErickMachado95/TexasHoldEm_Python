#Controls a game
import table, deck_of_cards

class Game:

    def __init__(self,game_name,num_players):
        self.game_name = game_name
        self.num_players = num_players
        self.table = table.Table()
        self.deck = deck_of_cards.Deck()
    
    def add_player(self,socket,player_name):
        self.table.add_player(table.Player(socket,player_name,100))
        
    def list_of_player_names(self):
        names = []
        for player in self.table.player_list:
            names.append(player.name)
        return names

    def list_of_players(self):
        return self.table.player_list
