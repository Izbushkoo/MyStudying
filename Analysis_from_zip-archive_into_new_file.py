import zipfile
import os


def analysis(file):

    # Have Latin alphabet low and capital letters, can create two dictionary with statistic

    alphabet = [chr(i) for i in range(97, 123)]
    alphabet_CAP = [chr(y) for y in range(65, 91)]
    letters_dict_lat = dict()
    letters_dict = dict()
    text = open(file, 'r', encoding='utf-8')

    # Here make the statistic by means of "app_dict()" according to where does the symbol in the text belong to

    for sym in text.read():
        if sym.isalpha():
            if sym in alphabet or sym in alphabet_CAP:
                app_dict(letters_dict_lat, sym)
            else:
                app_dict(letters_dict, sym)

    # Here I realized the value of "zip()" the very first time =)

    zip_strings = zip(sorting(letters_dict_lat), sorting(letters_dict))

    for element in zip_strings:
        full_string = '{:<50}\t'.format(element[0]) + '{:<50}\t\n'.format(element[1])
        write(full_string)

    text.close()


def sorting(dct):

    # For printing in one string Russian and Latin alphabet I had to create this part of code
    # for using this function making new string in "analysis()"

    strings_list = []

    for elem in sorted(dct.values(), reverse=True):
        for key in dct:
            if dct.get(key) == elem:
                strings_list.append((str(key) + ': ' + str(elem)))

    return strings_list


def app_dict(dct, elem):

    # Prevent repeating of code so here function fill in given dictionary.

    if elem not in dct.keys():
        dct[elem] = 1
    else:
        dct[elem] += 1


def write(obj):

    new_file.write(obj)


def clean_out(ask):

    # I decided to clean out after program
    # I tried to read the file exactly from archive, but it occurs some nonsense in the file =)

    os.remove(ask)


def ask(lst):

    # Ask a file name from user input and if the name in the list calls set of functions.
    # If not call function ask recursively.

    answer = input('\nEnter full-name of the file that you want to work with'
                   '(print "exit" for quitting): ')
    if answer in lst:
        zip_archive.extract(answer)
        analysis(answer)
        zip_archive.close()
        clean_out(answer)
        return
    elif answer == 'exit':
        return
    else:
        print('There is no such a file in archive!')
        ask(lst)

# In this main part create the archive file print list of files in it simultaneously creating a list of them
# for further checking of existing.

zip_archive = zipfile.ZipFile('voyna-i-mir.zip')
print('List of files in archive: ')
list_of_files_in_archive = []

for ind, file_i in enumerate(zip_archive.infolist()):
    print(str(ind + 1) + ') ' + str(file_i.filename))
    list_of_files_in_archive.append(file_i.filename)

# Open new file where wil be written the analysis into and write some title.

new_file = open('analysis.txt', 'w')
new_file.write('{:^60}\n'.format('Analysis of the text for every letter.'))
new_file.write('{:<50}'.format('Russian Letters') + '{:<50}\n'.format('Latin Letters'))

ask(list_of_files_in_archive)



