def print_num(start, num):
    if start == num:
        print(start)
        return start
    print(start)
    return print_num(start + 1, num)
num = int(input("Enter number: "))
start = 1
print_num(start, num)


