#  Function prints the numbers from start to num without using loops.


def print_num(start, stop):
    if start == stop:
        print(start)
        return start
    print(start)
    return print_num(start + 1, stop)


stop = int(input("Enter stop number: "))
start = int(input("Enter start number: "))
print_num(start, num)


