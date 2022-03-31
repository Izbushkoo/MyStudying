def move(n, x='A', y='B', z='C'):
    
    if n == 1:

        # If number of disk is equal for 1 it prints the last move and quit the recursion.

        print("Move disc 1 from rod {} to rod {}".format(x, y))
        return

    # Here we recursively call the function for the rest of disks that shifts them to auxiliary rod.

    move(n - 1, x, z, y)
    print("Move disc {} from rod {} to rod {}".format(n, x, y))
    move(n - 1, y, x, z)

number_of_disks = int(input("Enter a number of disks: "))
move(number_of_disks)
