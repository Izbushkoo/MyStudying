import random


class Cell:

    flag = True

    def __init__(self, number):
        self.number = number

    def is_spare(self):
        if self.flag:
            return True
        return False


class Board:

    def __init__(self):
        self.board = [Cell(x) for x in range(9)]


class Player:

    signs = ['X', 'O']

    def __init__(self, name):
        self.name = name
        self.filled_cells = []
        self.sign = self.signs.pop(self.signs.index(random.choice(self.signs)))

    def move(self, num):
        if board_1.board[num - 1].is_spare():
            board_1.board[num - 1].flag = False
            self.filled_cells.append(num)
            if self.check_win():
                return 'win'
            return True
        else:
            return False

    def check_win(self):
        wins_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                       (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        if len(self.filled_cells) >= 3:
            for elem in wins_tuples:
                if all(x in self.filled_cells for x in elem):
                    return True


def one_round(player):

    if any(x.flag for x in board_1.board):
        num = int(input("{} - {}: Enter cell number you want to fill in: ".format(player.name, player.sign)))
        if smth := player.move(num):
            if smth == 'win':
                print("{} won!".format(player.name))
                return True
            return False
        else:
            print("This cell is not empty.Try again.")
            one_round(player)
    else:
        return True


def print_board(plr_1, plr_2):

    count = 1
    for r in range(1, 4):
        for col in range(1, 4):
            if count in plr_1.filled_cells:
                print(plr_1.sign, '\t', end='')
            elif count in plr_2.filled_cells:
                print(plr_2.sign, '\t', end='')
            else:
                print(count, '\t', end='')
            count += 1
        print()


def main():

    global board_1
    flag = True
    board_1 = Board()
    player_1 = Player(input("Enter first player's name: "))
    player_2 = Player(input("Enter second's player name: "))

    while flag:
        for plr in (player_1, player_2):
            print_board(player_1, player_2)
            if one_round(plr):
                flag = False
                break
    print("Standoff!")


main()
