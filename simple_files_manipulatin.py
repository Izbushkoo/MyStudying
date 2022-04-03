text = open('numbers.txt', 'r')
summ = 0
for elem in text.read():
    if elem.isdigit():
        summ += int(elem)
text.close()

file = open('answer.txt', 'w')
file.write(str(summ))
file.close()


