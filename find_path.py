import os
def find_path(file):

    for root, dirs, files in os.walk(os.path.sep): # by means of "os.path.sep" it will work only with linux =)
        for name in files:
            if name == file:
                path_to = os.path.abspath(os.path.join(root, name))
                return path_to

file = 'something.txt'
