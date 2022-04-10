def count_let_dict(dct, lst):

    # Create a dictionary where key's a latin letter and value's a share of this letter in text counting only
    # latin letters

    for letter in lst:
        if letter not in dct.keys():
            dct[letter] = round((lst.count(letter) * 1 / len(lst)), 3)


def write(smth, file):

    file.write(smth)


def main_code():

    # Main part. Open two files one that exists and one new
    # by means of ".read()" reads it then make a list with all the latin letters found in the text,

    alphabet = tuple([chr(i) for i in range(97, 123)])
    file = open('text.txt', 'r')
    new_file = open('analysis.txt', 'w')
    text = file.read()
    lat_letters_list = []
    letters_count_dict = dict()

    for elem in text.lower():
        if elem in alphabet:
            lat_letters_list.append(elem)

    # calls function "count_let_dict()" and then working with created dictionary, print sorted shares according to
    # given conditions into new file with function "write()"

    count_let_dict(letters_count_dict, lat_letters_list)

    # I want to give a piece of explanation about my thinking. Having reversely sorted list of shares for every of them

    for item in sorted(letters_count_dict.values(), reverse=True):

        # search the nearest value of letter in sorted by alphabet keys of the dictionary.
        # And when find it, calls function "write()", write the string into new file.With help of ".pop()" method
        # get rid of this key from dictionary to prevent printing tha same letter every time and break the loop
        # for this share.
        
        for key in sorted(letters_count_dict):
            if letters_count_dict.get(key) == item:
                write((string :=
                      str(key) + ' ' + str(letters_count_dict.pop(key)) + '\n'),
                      new_file)
                break

    file.close()
    new_file.close()


main_code()

