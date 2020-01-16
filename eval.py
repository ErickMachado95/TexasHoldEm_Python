#Evaluation for cards
import deck_of_cards
 
card_eval = {"A_low": -1,"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"10":8,"J":9,"Q":10,"K":11,"A":12}
card_rank_eval = {"high":0,"one_pair":1,"two_pair":2,"three_kind":3,"straight":4,"flush":5,"full_house":6,"four_kind":7,"straight_flush":8}

def evalute_cards(community,hand):
    cards = community + hand
    order_cards(cards)
    hand, hand_cards = check_straight_flush(cards)
    if hand:
       return("straight_flush",hand_cards)
    hand, hand_cards = check_four_kind(cards)
    if hand:
        return("four_kind",hand_cards)
    hand,hand_cards = check_full_house(cards)
    if hand:
        return("full_house",hand_cards)
    hand, hand_cards = check_flush(cards)
    if hand:
        return("flush",hand_cards)
    hand, hand_cards = check_straight(cards)
    if hand:
        return("straight",hand_cards)
    hand, hand_cards = check_three_kind(cards)
    if hand:
        return("three_kind",hand_cards)
    hand, hand_cards = check_two_pair(cards)
    if hand:
        return("two_pair",hand_cards)
    hand, hand_cards = check_one_pair(cards)
    if hand:
        return("one_pair",hand_cards)
    hand, hand_cards = check_high_card(cards)
    if hand:
        return("high",hand_cards)
    return None #should never get to this line. 

#order cards from highest to lowest
def order_cards(cards):
    for i in range(1,len(cards)):
        for k in range(i,0,-1):
            if card_eval[cards[k].value] > card_eval[cards[k-1].value]:
                temp = cards[k]
                cards[k] = cards[k-1]
                cards[k-1] = temp
            else:
                break
    return


def check_high_card(cards):
    condition = True
    best_hand = []
    for i in range(0,5):
        best_hand.append(cards[i].value)

    return (condition,best_hand)

        
def check_one_pair(cards): 
    cards_c = cards.copy()
    condition = False
    best_hand = [[],[]]
    dic = {}
    for c in cards_c: 
        dic[c.value] = []

    for c in cards_c:
        dic[c.value].append(c)
        
    for i in dic: 
        if len(dic[i]) == 2:
            condition = True
            best_hand[0].append(dic[i][0].value)
            for j in dic[i]:
                cards_c.remove(j)
            for j in range(0,3):
                best_hand[1].append(cards_c[j].value)
            break

    return (condition,best_hand)


def check_two_pair(cards): 
    cards_c = cards.copy()
    condition = False
    best_hand = [[],[],[]]
    dic = {}
    
    for c in cards_c: 
        dic[c.value] = []
    for c in cards_c:
        dic[c.value].append(c)

    flag = False
    for i in dic: 
        if len(dic[i]) == 2:
            if not flag:
                flag = True
                best_hand[0].append(dic[i][0].value)
                for j in dic[i]:
                    cards_c.remove(j)
            else:
                condition = True
                best_hand[1].append(dic[i][0].value)
                for j in dic[i]:
                    cards_c.remove(j)
                best_hand[2].append(cards_c[0].value)         
                break
    return (condition,best_hand)

def check_three_kind(cards):
    cards_c = cards.copy()
    condition = False
    best_hand = [[],[]]
    dic = {}
    for c in cards_c: 
        dic[c.value] = []

    for c in cards_c:
        dic[c.value].append(c)
        
    for i in dic: 
        if len(dic[i]) == 3:
            condition = True
            best_hand[0].append(dic[i][0].value)
            for j in dic[i]:
                cards_c.remove(j)
            for j in range(0,2):
                best_hand[1].append(cards_c[j].value)
            break

    return (condition,best_hand)

def check_straight(cards):
    cards_c = cards.copy()
    condition = False
    best_hand = []
    dic = {}

    if cards_c[0].value == "A":
        cards_c.append(deck_of_cards.Card("Wild","A_low"))

    for c in cards_c: 
        dic[c.value] = c

    cards_c = []

    for i in dic:
        cards_c.append(dic[i])
    
    if len(cards_c) >= 5:
        for i in range(0,len(cards_c)-4):
            sequence = 0
            for j in range(i,i+4):
                if card_eval[cards_c[j].value] == card_eval[cards_c[j+1].value] + 1:
                    sequence += 1
            if sequence == 4:
                condition = True
                best_hand.append(cards_c[i].value)
                return(condition,best_hand)

    return(condition,best_hand)

def check_flush(cards): 
    cards_c = cards.copy()
    condition = False
    best_hand = []
    dic = {}
    for c in cards_c: 
        dic[c.suit] = []

    for c in cards_c:
        dic[c.suit].append(c)
        
    for i in dic: 
        if len(dic[i]) >= 5:
            condition = True
            for j in range(0,5):
                best_hand.append(dic[i][j].value)
            break

    return (condition,best_hand)


def check_full_house(cards):
    cards_c = cards.copy()
    condition = False
    best_hand = [[],[]]
    dic = {}
    for c in cards_c:
        dic[c.value] = []
    for c in cards_c:
        dic[c.value].append(c)

    high_pair = False
    high_three = False

    for i in dic:
        if len(dic[i]) == 3 and not high_three:
            high_three = True
            best_hand[0].append(dic[i][0].value)
            continue
        if len(dic[i]) >= 2 and not high_pair:
            high_pair = True
            best_hand[1].append(dic[i][0].value)
    if (not len(best_hand[0]) == 0) and (not len(best_hand[1]) == 0):
        condition = True

    return (condition,best_hand)



def check_four_kind(cards):
    cards_c = cards.copy()
    condition = False
    best_hand = [[],[]]
    dic = {}

    for c in cards_c: 
        dic[c.value] = []

    for c in cards_c:
        dic[c.value].append(c)
        
    for i in dic: 
        if len(dic[i]) == 4:
            condition = True
            best_hand[0].append(dic[i][0].value)
            for j in dic[i]:
                cards_c.remove(j)
            for j in range(0,1):
                best_hand[1].append(cards_c[j].value)
            break

    return (condition,best_hand)


def check_straight_flush(cards):
    cards_c = cards.copy()
    condition = False
    best_hand = []
    dic = {}

    for c in cards_c.copy():
        if c.value == "A":
            cards_c.append(deck_of_cards.Card(c.suit,"A_low"))


    for c in cards_c:
        dic[c.suit] = []

    for c in cards_c:
        dic[c.suit].append(c)

    for i in dic:
        if len(dic[i]) >= 5:
            for j in range(0,len(dic[i])-4):
                sequence = 0
                for k in range(j,j+4):
                    if card_eval[dic[i][k].value] == card_eval[dic[i][k + 1].value] + 1:
                        sequence += 1
                if sequence == 4:
                    condition = True
                    best_hand.append(dic[i][j].value)
                    return(condition,best_hand)
    return (condition, best_hand)
