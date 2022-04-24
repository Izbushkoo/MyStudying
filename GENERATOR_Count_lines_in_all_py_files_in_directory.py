import os
from typing import Optional
from collections.abc import Iterable,Generator


def find_root() -> str:
    """
    Find root directory according to OS.

    Returns: '/' or 'ROOT-DISK'
    rtype: str

    """

    if os.name == 'nt':
        return os.path.splitdrive(os.path.abspath('smth'))[1]
    else:
        return os.path.sep


def find_path(directory: str) -> Optional[str, None]:
    """
    Find full path from root to chosen directory.

    Args:
        directory: Chosen by user directory

    Returns: Full path to chosen directory or None.
    rtype: str/None

    """
    if directory.endswith(os.path.sep):
        directory = directory[:-1]
    if directory.startswith(find_root()) or directory.startswith(os.path.sep):
        directory = directory[1:]

    for root, dirs, files in os.walk(find_root()):  # The same as in 3 task, can take a while.Not optimal one=)
        for i_dir in dirs:
            if os.path.split(directory)[1] == i_dir:
                return os.path.join(root, directory)
    return


def string_counter(chosen_dir: str) -> Optional[Iterable[str], None]:
    """
    Generator that counts lines all through ".py" files not paying attention to empty or commented lines.

    Args:
        chosen_dir: Full path to chosen by user directory.

    Returns: Generator or None

    """

    def work_with_file(path_to_file: str) -> int:
        """
        Function opens pointed file, reads and count lines in it.
        Args:
            path_to_file: Pointed path to the file for reading.

        Returns: Number of strings in the file
        rtype: int
        """
        print("Counting inside:", path_to_file)
        count = 0
        with open(path_to_file, 'r') as file:
            for i_line in file:
                if i_line[:-1].startswith('#') or i_line[:-1] == "":
                    pass
                else:
                    count += 1
            return count

    dirs_list = [os.path.join(chosen_dir, elem) for elem in os.listdir(chosen_dir)]
    string_count = 0

    while True:
        if dirs_list:
            try:
                for i_dir in dirs_list:
                    if i_dir.endswith('.py'):
                        string_count += work_with_file(i_dir)
                        yield string_count
                    elif os.path.isdir(i_dir):
                        dirs_list.extend((os.path.join(i_dir, x) for x in os.listdir(i_dir)))
                    dirs_list.pop(dirs_list.index(i_dir))
            except PermissionError:  # Not Everybody has root access =)
                pass

        else:
            return


def show(gen: Generator) -> None:
    """
    Prints values of generator.

    Args:
        gen: Generator with counter of lines.

    """
    for elem in gen:
        print('\nCurrent number of lines:', elem)


dirct = input("Enter a directory: ")

if os.path.exists(dirct):
    show(string_counter(dirct))
elif dirct == "":
    show(string_counter(find_root()))
else:
    ask = input("Directory not found.Enter full path or try to search!\n"
                "Type 'yes' for searching through: ").lower()
    if ask == 'yes':
        if dirct := find_path(dirct):
            print("Path is found:", dirct)
            print("\nScript is running...\n")
            show(string_counter(dirct))
        else:
            print("Path is not found!")
