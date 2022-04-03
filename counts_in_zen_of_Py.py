import os

def find_path(file):

    path = os.path.abspath(os.path.join('..', '..'))  # Decrease the time of search =)

    for root, dir, files in os.walk(path):
        for name in files:
            if name == file:
                return os.path.abspath(os.path.join(root, name))


def work_with_file(file):
    zen = open(file, 'r')
    let_dict = dict()
    words_count = 0
    str_count = 0
    letters_count = 0
    for string in zen:
        str_count += 1
        words_count += len(string.split())
        for elem in string.lower():
            if elem.isalpha():
                letters_count += 1
                if not let_dict.get(elem):
                    let_dict[elem] = 1
                else:
                    let_dict[elem] = let_dict.get(elem) + 1
    zen.close()


    minimum = min(let_dict.values())

    min_list = []
    for key in let_dict.keys():
        if let_dict.get(key) == minimum:
            min_list.append(key)

    print('Quantity of letters in file:', letters_count)
    print('Quantity of words in file:', words_count)
    print('Quantity of strings in file:', str_count)
    print('The least used letter(s):', ', '.join(min_list))

work_with_file(find_path('zen.txt'))


