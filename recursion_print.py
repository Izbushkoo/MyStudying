#  Function prints numbers from "start" to "stop" without using loops.

def print_num(start, stop):
    if start == stop:
        print(start)
        return start
    print(start)
    return print_num(start + 1, stop)


stop = int(input("Enter stop number: "))
start = int(input("Enter start number: "))
print_num(start, num)


# This one prints numbers from 1 to Stop.

def print_num_stop(stop):
    
    if stop == 0:
        return stop
    print_num_stop(stop - 1)
    print(stop)


stop_1 = int(input("Enter stop number: "))
print_num(stop_1)

