import random


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:

    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']  # Quite an unnecessary classification =)
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K", "A"]

    def __init__(self):
        self.deck = [Card(r, s) for r in self.ranks for s in self.suits]

class Player:


    scores = 0

    def __init__(self, name):
        self.name = name
        self.cards = []

    def find_scores(self):

        local_scores = 0
        for card in self.cards:
            if isinstance(card.rank, int):
                local_scores += card.rank
            elif card.rank == 'A':
                if local_scores + 11 < 21:
                    local_scores += 11
                else:
                    local_scores += 1
            else:
                local_scores += 10
        self.scores = local_scores
        return local_scores

def game(deal, plr):

    deck_1 = Deck()
    for pr in (deal, plr):
        for _ in range(2):
            pr.cards.append(deck_1.deck.pop(deck_1.deck.index(random.choice(deck_1.deck))))
        pr.find_scores()
    print("Your hand: ", end='')
    for card in plr.cards:
        print("{}: {}".format(card.rank, card.suit), end=' | ')
    print("Scores:", plr.scores)
    while plr.scores < 21:
        ask = input('More(yes/no)? ').lower()
        if ask == "yes":
            plr.cards.append(deck_1.deck.pop(deck_1.deck.index(random.choice(deck_1.deck))))
            print(plr.find_scores())
        elif ask == "no":
            break
    check_result(deal, plr)
    for pr in (deal, plr):
        pr.cards = []
        pr.scores = 0

def check_result(deal, plr):
    if plr.scores <= 21:
        print("Dealer hand:", end=' ')
        for card in deal.cards:
            print("{}: {} ".format(card.rank, card.suit), end=' | ')
        print("Scores:", deal.scores)
        if deal.scores == plr.scores:
            print("Standoff!")
        elif deal.scores > plr.scores:
            print("Dealer won!")
        else:
            print("Player won!")
    else:
        print("Dealer won!")


dealer = Player('Dealer')
name = input("Enter your name: ")
player = Player(name)
question = input("Let's play(yes/no)?").lower()
while question == 'yes':
    game(dealer, player)
    question = input('\nOne more time?')
