import os.path

# This thing take path-input and recursively counts numbers of files, subdirectories and total size,
# putting all the values in the list.

def go_through_2(path, count_list):

    # index.0 is number of subdirectories
    # index.1 is number of files
    # index.2 is sum of sizes of files

    if os.path.isfile(path):
        count_list[1] += 1
        count_list[2] += os.path.getsize(path)
        return
    else:
        for elem in os.listdir(path):
            if os.path.isdir(new_path := os.path.join(path, elem)):
                count_list[0] += 1
            go_through_2(new_path, count_list)


count_list = [0, 0, 0]
path = input("Please, enter a path to directory: ")
go_through_2(path, count_list)

print("Directory size (Kb):", count_list[2] / 1024)
print("Numbers of subdirectories:", count_list[0])
print("Numbers of files:", count_list[1])

