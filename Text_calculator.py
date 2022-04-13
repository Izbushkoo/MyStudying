
# Here is two option of text calculators.First one just counts from text file in format
# 10 / 10  and print summ of all lines of the file.
# Second calc additional catches exceptions and proposes to fix this line.
# If "yes" count new line otherwise continue count the rest lines

def first_option():

    def split(line):

        try:
            string_list = line.split()
            if not string_list[0].isdigit() and string_list[2].isdigit():
                raise ValueError
            if answer := eval(line[:-1]):  # Cut '\n'
                return answer
        except ValueError:
            return 0
            # print("Incorrect value.")
        except SyntaxError:
            return 0
            # print("Invalid operand.")
        return 0

    summa = 0
    with open('calc.txt', 'r') as file:
        for i_line in file:
            summa += split(i_line)
    print(summa)


def second_option():

    def manipulations(line):

        try:
            string_list = line.split()
            if not string_list[0].isdigit() and string_list[2].isdigit():
                raise ValueError
            if answer := eval(line):
                return answer
        except ValueError:
            return fix(input("There is a mistake in operands {}   Want to fix(type 'yes')? "
                             .format(line)).lower())
        except SyntaxError:
            return fix(input("There is a mistake in operation {}   Want to fix(type 'yes')? "
                             .format(line)).lower())
        except IndexError:
            return fix(input("There is a mistake, not enough operands {}   Want to fix(type 'yes')? "
                             .format(line)).lower())
        except ZeroDivisionError:
            return fix(input("Can't divide by 0 {}   Want to fix(type 'yes')? "
                             .format(line)).lower())

    def fix(ans):

        if ans == 'yes':
            fixed_line = input('Enter fixed line: ')
            return manipulations(fixed_line)
        return 0

    summ = 0
    with open('calc.txt', 'r') as file:
        for i_line in file:
            summ += manipulations(i_line[:-1])
    print("Summ of results:", summ)


# first_option()
# second_option()

