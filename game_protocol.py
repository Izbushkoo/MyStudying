def cut_name(elem):

    lst = elem.split()
    name = lst[1][0] + '. ' + lst[0]
    if int(lst[2]) > k:
        string_dict[name] = int(lst[2])


def sort():
    sorted_list_of_values = sorted(string_dict.values())[::-1]
    print(sorted_list_of_values)
    for ind in range(len(sorted_list_of_values)):
        for key, value in string_dict.items():
            if string_dict.get(key) == sorted_list_of_values[ind]:
                string = str(ind + 1) + ') ' + key + ' ' + str(string_dict.get(key))
                file.write(string + '\n')


first_tour = open('first_tour.txt', 'r')
file = open('second_tour.txt', 'w')
file.write(str(2) + '\n')
list_of_strings = [string[:-1] for string in first_tour]

global string_dict, k
string_dict = dict()
k = int(list_of_strings.pop(0))
for item in list_of_strings[1:]:
    cut_name(item)
sort()
first_tour.close()
file.close()

