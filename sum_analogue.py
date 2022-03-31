#  It is the analog of sum.function that can summarize list of lists and
#  and unlimited quantity of numbers.

def unpack(object):
    
    #  Unpack the list of lists into one by means of recursion.
    
    if object == []:
        return object

    if isinstance(object[0], list):
        return unpack(object[0}) + unpack(object[1:])
    return object[:1] + unpack(object[1:})


def sum(*args):

    #  Function gets the sum if argument is a list or any kind of numbers
    #  or print error message.
    
    summ = 0
    for object in args:
        if isinstance(object, list):
            for el in unpack(object):
                summ += el
        elif isinstance(object, (int, float)):
            summ += object
        else:
            return "Input error."

    return summ

