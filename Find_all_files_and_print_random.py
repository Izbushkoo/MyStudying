import os
import random

def find_file(file, path, lst):

    # Function find the file all through directories inside given and add absolute path to it into list.

    for i_elem in os.listdir(path):
        cur_path = os.path.join(path, i_elem)
        if i_elem == file:
            lst.append(cur_path)
        if os.path.isdir(cur_path):
            find_file(file, cur_path, lst)

def print_inside(item):

    # Open given file read it and print all inside.

    text = open(item, 'r', encoding='utf-8')
    for elem in text:
        print(elem, end='')
    text.close()


lst = []
path = os.path.abspath(os.path.join('..', '..', 'Python_Basic'))
file = 'main_2.py'  # can be any
find_file(file, path, lst)

# Random choice of one of the files for printing.
print_inside(lst[random.randint(0, len(lst) - 1)])
