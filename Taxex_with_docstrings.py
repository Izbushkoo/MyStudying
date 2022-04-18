from termcolor import colored

class Property:
    """
    Base class that describes property

    Args:
         worth (float/int): pass worth of property.

    Attributes:
        share (int) : share of worth that need to be paid as tax.

    """
    def __init__(self, worth):
        self.worth = worth
        self.share = 1

    def __str__(self):
        return self.__class__.__name__

    def tax(self):
        """

        Method for calculating tax.

        :return: rounded meaning of tax
        :rtype: float
        """
        return round(self.worth / self.share, 2)

class Apartment(Property):
    """
    class Apartment Parent: Property

    Args:
        worth (float/int): pass worth of property.

    Attributes:
        share (int) : share of worth that need to be paid as tax.

    """
    def __init__(self, worth):
        super().__init__(worth)
        self.share = 1000

class Car(Property):
    """
    class Car Parent: Property

    Args:
        worth (float/int): pass worth of property.

    Attributes:
        share (int) : share of worth that need to be paid as tax.

    """
    def __init__(self, worth):
        super().__init__(worth)
        self.share = 200

class CountryHouse(Property):
    """
    class CountryHouse Parent: Property

    Args:
        worth (float/int): pass worth of property.

    Attributes:
        share (int) : share of worth that need to be paid as tax.

    """
    def __init__(self, worth):
        super().__init__(worth)
        self.share = 500


class MyValueException(Exception):

    """ class MyValueException Parent: Exception """

    pass


class Human:
    """
    class Human that describes a person.

    Args:
        name (str) : Name of person.

    Attributes:
        property (list) : List that will contain examples of Property classes.
        money (int) : amount of money of a person.
    """
    property = []

    def __init__(self, name):
        self.set_name(name)
        self.__money = 0

    def __str__(self):
        info = "Name: " + colored("{name}".format(name=self.__name), 'yellow') + "\nProperty:\n{no:*^40}\n"\
            .format(no=' None ' if self.property == [] else '')

        for item in self.property:
            info += "\n{cl_name:*^40}\nWorth: {worth:*^40}\nTax: {tax:*^40}\n"\
                .format(cl_name=str(item),
                        worth=str(item.worth), tax=str(item.tax()))
        return info

    def get_name(self):
        """
        getter for person name

        :return: __name
        :rtype: str

        """
        return self.__name

    def set_name(self, name):
        """
        setter for person's name
        :param name: __name
        :type name: str
        :return: none
        :raise MyValueException: is called if name consist of anything but letters.
            then ask param new_name: (str) and recursively calls self.set_name.

        """
        try:
            if name.isalpha():
               self.__name = name.capitalize()
               return
            else:
                raise MyValueException
        except MyValueException:
            print("Name must consist of letters only!")
            new_name = input("Enter your Name: ")
            self.set_name(new_name)

    def get_money(self):
        """
        getter for money.
        :return: __money rounded money of person.
        :rtype; (float/int)
        """
        return round(self.__money, 2)

    def set_money(self, money):
        """
        setter for money.
        :param money: __money
        :type: (float/int)
        :return: none
        :raise MyValueException: is called if money is negative number.
            then ask param new_money: (str) - to prevent stopping of
            program and recursively calls self.set_name.
        :exception TypeError: ask param new_money: (float/int)
            then recursively calls self.set_name.
        """
        try:
            if money < 0:
                raise MyValueException
            self.__money = money
            return
        except MyValueException:
            print("Amount of money can't be negative!")
            new_money = input("Enter amount of money: ")
            self.set_money(new_money)
        except TypeError:
            print("Amount of money must be a number!")
            new_money = float(input("Enter amount of money: "))
            self.set_money(new_money)

    def total_tax(self):
        """
        finding total tax summ of all property in person possessing.
        :return: total
        :rtype: (float/int)
        """
        total = 0
        for item in self.property:
            total += item.tax()
            # print(item.tax())
        return total

    def is_enough_money(self):
        """
        Checking whether the money is enough to pay tax.
        print all necessary information about it enough or not and the difference
        if it is not.

        """
        total_tax = self.total_tax()
        if self.__money >= total_tax:
            print("Your total tax to pay: {tax}\nYou have enough money: {money}"
                   .format(tax=total_tax, money=self.__money))
        else:
            print("Your total tax to pay: {tax}"
                  "\nYou don't have enough money: {money}"
                  "\nYou need {difference} more."
                  .format(tax=total_tax, money=self.__money, difference=total_tax - self.__money)
                  )

def create_prop(man, item):
    """
    Creating of sample of class property.
    :param man: is a person who the property will belong to.
    :type man: class Human
    :param item: is a name for definition what daughter class is need to be created
    :type item: (str)
    :except ValueError: is called if atribute worth is not (float/int) type
    """
    key_words = ('car', 'apartment', 'country-house', 'countryhouse', 'country house')
    if item in key_words:
        while True:
            try:
                worth = float(input("Worth of {prop_item}: ".format(prop_item=item)))
            except ValueError:
                print("You must enter the number!")
            else:
                break
        if item == 'car':
            man.property.append(Car(worth))
        elif item == 'apartment':
            man.property.append(Apartment(worth))
        elif item == 'country-house' or 'countryhouse' or 'country house':
            man.property.append(CountryHouse(worth))


def main():
    """
    Main part of program that ask a name, create a sample of Human class,
    ask about amount of money make a try and call except ValueError if it is not number
    then set the money quantity for the person. Ask about property and create it.
    Finally print all the info thad person need to know about his taxes property and money.

    """
    man = Human(name := input("Enter your Name: "))

    while True:
        try:
            money = float(input("How much money do you have? "))
        except ValueError:
            print("You must enter the number!")
        else:
            break

    man.set_money(money)

    prop = input("What kind of property do you have?\n"
                 "{:*^40}\nCount through coma and space: "
                 .format(' Car, Apartment, Country-House ')).lower().split(', ')
    if prop == ['']:
        pass
    else:
        for elem in prop:
            create_prop(man, elem)

    print('\n', man)

    man.is_enough_money()


main()