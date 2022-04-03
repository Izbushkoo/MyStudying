import os

def find_path(item):
    # Knowing the nearest point we're searching for absolute path to file.
    for root, dirs, files in os.walk(os.path.abspath(os.path.join('..', '..', 'Desktop'))):
        for name in files:
            if name == item:
                path_to = os.path.abspath(os.path.join(root, name))
                return path_to


file = open(find_path('group_1.txt'), 'r')
# make a list of the first group scores
score_lst = []
for i_line in file:
    score_lst.append(int(i_line.split()[2]))
# find the score difference
difference = score_lst[0]
for item in score_lst[1:]:
    difference -= item

file_2 = open(find_path('group_2.txt'), 'r')
# find the result of multiplying of the second group scores
result = 1
for i_line in file_2:
    result *= int(i_line.split()[2])
# print summ, difference and result
print('Sum of scores of the first group:', sum(score_lst))
print('Difference of scores of the first group:', difference)
print('Compose of scores of the first group:', result)
