import random
import time
import threading

# It was bloody battle against the task that I create inside my mind. But I won according to my vision
# but if there is any optimisation or advice or whatever it is you are welcome=)

class Potato:

    ripe_states = {0: 'seed', 1: 'sprout', 2: 'not rape', 3: 'rape'}

    def __init__(self, number):
        self.number = number
        self.ripe_state = 0

    def info(self):
        print('Potato {} is {}'.format(self.number, self.ripe_states[self.ripe_state]))

    def grow(self):
        if self.ripe_state < 3:
            self.ripe_state += 1

    def is_ripe(self):
        if self.ripe_state == 3:
            return True
        return False


class PotatoGarden:

    state_of_garden = {0: 'fine',
                       1: 'weeded',
                       2: 'weeded and full of beatles',
                       3: 'weeded,full of beatles and diseases',
                       4: 'dead'
                       }

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]
        self.state = 0

    def info(self):
        for i_potato in self.potatoes:
            print("Potato {} is {}".format(i_potato.number, i_potato.ripe_state))

    def grow_all(self):
        if self.potatoes:
            for i_potato in self.potatoes:
                i_potato.grow()
        return False

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):

            return False
        else:

            return True


class Gardener:

    garden_bed = 'nothing'

    def __init__(self, name):
        self.name = name

    def plant(self):
        try:
            how_many_potatoes = int(input("How many potatoes in the garden bed? "))
        except ValueError:
            print("You must enter a number!")
            self.plant()
        else:

            self.garden_bed = PotatoGarden(how_many_potatoes)
            return

    def harvest(self):
        harvest = round(len(self.garden_bed.potatoes) * random.uniform(5, 15), 2)
        self.garden_bed = PotatoGarden(0)
        print('\nPotato was harvested.The harvest: {}kg'.format(harvest))
        return harvest

    def care(self):
        if self.garden_bed.state > 0:
            self.garden_bed.state = 0
            print("The gardener have took care of the garden bed.")


def thread_func(gardener):

    while not stop:
        time.sleep(random.uniform(1, 3))
        while True:
            if not isinstance(gardener.garden_bed, str):
                break
        if gardener.garden_bed.state < 4 and not gardener.garden_bed.are_all_ripe():
            print("\nNow the garden bed is {}"
                  .format(gardener.garden_bed.state_of_garden[gardener.garden_bed.state]))
            gardener.garden_bed.state += 1
        pass


def gardener_work(gardener):

    total_harvest = 0

    def should_plant():

        ask = input("Should gardener {} plant potatoes(yes/no)? "
                    .format(gardener.name)).lower()
        if ask == 'yes':
            gardener.plant()
            return True
        elif ask == 'no':
            print("The Gardener's total harvest:", total_harvest)
            return False

    while True:
        time.sleep(6)
        if gardener.garden_bed.are_all_ripe():
            print("All potatoes are ripe and can be harvest.")
            total_harvest += gardener.harvest()
            if not should_plant():
                return
        else:
            print("Potatoes are not ripe yet.")
            if gardener.garden_bed.state < 4:
                gardener.garden_bed.grow_all()
                gardener.care()
            else:
                print("The garden bed is dead.")
                gardener.garden_bed = PotatoGarden(0)
                if not should_plant():
                    return False


def main():

    global stop
    stop = False
    gardener_name = str(input("Enter gardener's name: "))
    gardener = Gardener(gardener_name)
    whether_pass = str(input("Do you want to pass any garden bed to {}(yes/no)? "
                             .format(gardener.name))).lower()
    if whether_pass == 'yes':
        gardener.plant()
        x = threading.Thread(target=thread_func, args=(gardener,))
        x.start()
        if not gardener_work(gardener):
            stop = True
        while x.is_alive():
            pass

    else:
        return


main()
