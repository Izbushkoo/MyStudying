# Work with exceptions.
# Have a file with names in every line, find the sum of symbols in every that are not less than 3,
# not counting literal "\n", otherwise throw exception and log it into new file and print sum anyway.

def work_with_string(item, count):

    try:
        length = len(item)
        if item.endswith('\n'):
            length -= 1
        if length < 3:
            raise BaseException
    except BaseException:
        error = "Line {}: {}. Here is less than 3 symbols.\n".format(count, item[:-1])
        print(error)
        with open('errors.log', 'a') as log_file:
            log_file.write(error)
        return 0
    else:
        return length


summ = 0
with open('people.txt', 'r', encoding='utf-8') as people_file:

    for ind, i_string in enumerate(people_file):
        summ += work_with_string(i_string, ind + 1)

print("Total amount of symbols:", summ)
print(people_file.closed)