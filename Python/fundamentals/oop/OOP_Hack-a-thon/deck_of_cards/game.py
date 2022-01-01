from classes.deck import Deck
import random
bicycle = Deck()
random.shuffle(bicycle.cards)
player1_name = input("What is Player 1's name? ")
player2_name = input("What is Player 2's name? ")
player1_hand = []
player2_hand = []
round = 1
rand_list = []

def player1_wins():
    print(player1_name.upper() + " WINS THE GAME!")
    quit()

def player2_wins():
    print(player2_name.upper() + " WINS THE GAME!")
    quit()

def popx(x):
    player1_hand.pop(x)
    player2_hand.pop(x)

def rand_list_shuffle (index):
    rand_list.clear()
    rand_list.append (player1_hand[index])
    rand_list.append (player2_hand[index])
    random.shuffle(rand_list)

def war(p1, p2, card_counter):
    print("WAR")
    if len(player1_hand) <= card_counter:
        player2_wins()
    elif len(player2_hand) <= card_counter:
        player1_wins()
    else:
        print("    " + player1_name + " plays " + str(p1[card_counter].point_val))
        print("    " + player2_name + " plays " + str(p2[card_counter].point_val))
    if len(p1) >= card_counter and len(p2) >= card_counter:
        if p1[card_counter].point_val > p2[card_counter].point_val:
            print("    " + player1_name + " wins the hand.")
            for x in range (0, card_counter+1):
                rand_list_shuffle(x)
                p1.append(rand_list[0])
                p1.append(rand_list[1])
            for x in range(card_counter, -1, -1):
                popx(x)
        elif player2_hand[card_counter].point_val > player1_hand[card_counter].point_val:
            print("    " + player2_name + " wins the hand.")
            for x in range (0, card_counter+1):
                rand_list_shuffle(x)
                p2.append(rand_list[0])
                p2.append(rand_list[1])
            for x in range(card_counter, -1, -1):
                popx(x)
        else:
            new_counter = card_counter + 4
            war (player1_hand, player2_hand, new_counter)
    elif len(player1_hand) == 0:
        player2_wins()
    elif len(player2_hand) == 0:
        player1_wins()

for x in range(52):
    if x % 2 == 0:
        player2_hand.append(bicycle.cards[x])
    else:
        player1_hand.append(bicycle.cards[x])

print ("After deal, " + player1_name + " has " + str(len(player1_hand)) + " cards.")
print ("After deal, " + player2_name + " has " + str(len(player2_hand)) + " cards.")
print (" ")

while min(len(player1_hand), len(player2_hand)) > 0:
    print("Round " + str(round))
    rand_list_shuffle(0)
    print(player1_name + " plays " + str(player1_hand[0].point_val))
    print(player2_name + " plays " + str(player2_hand[0].point_val))
    if player1_hand[0].point_val > player2_hand[0].point_val:
        print(player1_name + " wins the hand.")
        player1_hand.append(rand_list[0])
        player1_hand.append(rand_list[1])
        popx(0)
    elif player2_hand[0].point_val > player1_hand[0].point_val:
        print(player2_name + " wins the hand.")
        player2_hand.append(rand_list[0])
        player2_hand.append(rand_list[1])
        popx(0)
    else:
        war (player1_hand, player2_hand, 4)
    print (player1_name + " has " + str(len(player1_hand)) + " cards.")
    print (player2_name + " has " + str(len(player2_hand)) + " cards.")
    print (" ")
    round = round + 1
    if len(player1_hand) + len(player2_hand) !=52:
        print("The card count is incorrect.")
        break

if len(player1_hand) == 0:
    player2_wins()
elif len(player2_hand) == 0:
    player1_wins()