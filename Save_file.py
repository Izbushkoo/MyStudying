import os


def write(string, path):

    file = open(path, 'w')
    file.write(string)
    file.close()


def root_dir(smth):

    #  Here function returns root directory.

    if os.path.split(smth)[1] == '':
        return os.path.split(smth)[0]
    path = root_dir(os.path.split(smth)[0])
    return path


def walk(dir, path):

    #  In this part we are checking the path to the first directory of input string
    #  and return False if not found.

    for root, dirs, files in os.walk(root_dir(os.path.abspath('smth'))):
        for name in dirs:
            if dir == name and os.path.exists(full_path := os.path.abspath(os.path.join(root, path))):
                return full_path

    return False


def save():

    # Here function splits entered string of directories and makes some checks.

    save_place = input("\nWhere want to save the document(enter sequence of directories through spaces): ") \
        .split()
    path = os.path.sep.join(save_place)
    if save_place == []:

        # If list is empty, the place of saving will be current working directory.Then calls the "file_name()"

        full_path = os.getcwd()
        file_name(full_path)
        return

    elif (full_path := walk(save_place[0], path)):

        # If there are any directories in list and if "walk()" returns not False function calls "file_name()"

        file_name(full_path)

    else:

        # Otherwise, prints "Error message" and calls "save()" for new inquire of directories.

        print("\n", path, "\nError.Not found such a path! ")
        save()


def file_name(full_path):

    # And here function asks the name of file makes full path to file and if file exists asks
    # what to do (overwrite or no) if "no" calls "file_name()"
    # and in any other case exit of function.

    file = input("\nEnter a file name: ") + '.txt'
    full_path_to_file = os.path.join(full_path, file)

    if os.path.exists(full_path_to_file):
        ask = input("\nFile exists already, want to overwrite it?(Y/N): ").lower()

        if ask == 'y':
            write(string, full_path_to_file)
            print("\nSuccessfully overwritten!")
            return True
        if ask == 'n':
            file_name(full_path)
        else:
            return
    else:
        write(string, full_path_to_file)
        print('\nSuccessfully saved!')
        return True

global string
string = input("Enter a string: ")
save()

