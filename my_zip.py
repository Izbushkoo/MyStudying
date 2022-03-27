def min_len(*args):
    # Finds the minimum of lenths of objects.

    lenths = [len(elem) for elem in args]
    return min(lenths)


def my_zip(*args):
    lst = [[] for _ in range(min_len(*args))]
    for elem in args:
        for i, value in enumerate(elem):
            if i < len(lst):
                lst[i].append(value)
            else:
                break

    lst_of_tpls = (tuple(obj) for obj in lst)
    return lst_of_tpls

# The data for checking
# a = [1, 2, 3, 4, 5]
# b = {1: 's', 2: 'q', 3: 4}
# x = (1, 2, 3, 4, 5)
# print(my_zip(a, b, x))