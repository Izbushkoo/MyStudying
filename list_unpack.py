def new_list(lst, full_list=[]):

    # This was created on my own.

    if isinstance(lst, (int, float, str)):
        return lst
    for elem in lst:
        if isinstance(new_list(elem), (int, float, str)):
            full_list.append(new_list(elem))

    return full_list


def new_list_2(lst_2):

    # this thing was peeked on google =) I got the general idea
    # but first option for me is more instinctively understandable.
    # and this version is almost two time faster then mine =))

    if lst_2 == []:
        return lst_2
    if isinstance(lst_2[0], list):
        return new_list_2(lst_2[0]) + new_list_2(lst_2[1:])

    return lst_2[:1] + new_list_2(lst_2[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
