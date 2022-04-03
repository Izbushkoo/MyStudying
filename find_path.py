import os
def find_path(file):

    for root, dirs, files in os.walk(os.path.sep):
        for name in files:
            if name == file:
                path_to = os.path.abspath(os.path.join(root, name))
                return path_to

file = 'something.txt'
