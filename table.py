#table module similar to a physical table in poker

class Player:
    def __init__(self,name,chips):
        self.name = name
        self.chips = chips
        self.hand = {}

 
    def sub_chips(self,amount):
        """Subtracts 'amount' from player chips and returns new value"""
        self.chips = self.chips - amount
        return self.chips

    def add_chips(self,amount):
        """Adds 'amount' to player chips and returns new value"""
        self.chips = self.chips + amount
        return self.chips
    
    def set_hand(self,hand):
        """Sets new hand for plyaer"""
        self.hand = hand



class Table:  
    def __init__(self):
        self.player_list = []
        self.pot = 0


    def player_exists(self,player_name):
        """Returns true if a player exists (based on name), false otherwise"""
        if self.player_list > 0:
            for player in self.player_list:
                if player.name == player_name:
                    return True
        return False
    def add_player(self,player):
        """Adds player to the table. Returns true if added, false otherwise"""
        if len(self.player_list) < 10 and not self.player_exists(player.name): 
            self.player_list.append(player)
            return True
        else: 
            return False

    def remove_player(self,player_name):
        """Removes player from table (if player exists)"""
        if self.player_list > 0: 
            for index,player in enumerate(self.player_list.copy()):
                if player.name == player_name:
                    self.player_list.remove(index)
                    break
    
