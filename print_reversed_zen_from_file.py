strings_list = []
zen = open('zen.txt', 'r')
for string in zen:
    strings_list.insert(0, string)
zen.close()
strings_list[0] += '\n'
print(''.join(strings_list))


