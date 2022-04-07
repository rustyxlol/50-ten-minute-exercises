"""
redefine the mysum function we defined in chapter 1,
such that it can take any number of arguments. The arguments must all be of the
same type and know how to respond to the + operator. (Thus, the function should
work with numbers, strings, lists, and tuples, but not with sets and dicts.)



BEYOND THE EXERCISE
✅ Write a function, mysum_bigger_than, that works the same as mysum, except that
it takes a first argument that precedes *args. That argument indicates the
threshold for including an argument in the sum. Thus, calling mysum_bigger
_than(10, 5, 20, 30, 6) would return 50—because 5 and 6 aren't greater than
10. This function should similarly work with any type and assumes that all of the
arguments are of the same type. Note that > and < work on many different types
in Python, not just on numbers; with strings, lists, and tuples, it refers to their
sort order



✅ Write a function, sum_numeric, that takes any number of arguments. If the
argument is or can be turned into an integer, then it should be added to the
total. Arguments that can't be handled as integers should be ignored. The
result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a', '30',
'bcd') would return 60. Notice that even if the string 30 is an element in the
list, it's converted into an integer and added to the total


✅ Write a function that takes a list of dicts and returns a single dict that combines
all of the keys and values. If a key appears in more than one argument, the
value should be a list containing all of the values from the arguments. 
"""


from multiprocessing.sharedctypes import Value


def mysum(*items):
    if not items:
        return items

    output = items[0]
    for item in items[1:]:
        output += item
    return output


def mysum_bigger_than(threshold, *items):
    if not items:
        return items

    output = None
    sumit = False

    for item in items:
        if item > threshold:
            if sumit:
                output += item
            else:
                output = item
                sumit = True
    return output


def sum_numeric(*items):
    if not items:
        return items

    output = 0

    for item in items:
        try:
            output += int(item)
        except ValueError:
            print("Encountered non integer: ", item)
    return output


def merge_dicts(dict1, dict2):
    # output = dict1
    # for key, value in dict2.items():
    #     output[key] = value
    # return output
    return {**dict1, **dict2}


if __name__ == "__main__":
    print(mysum([1, 2, 3], [4, 5, 6]))
    print(mysum('abc', 'def'))
    print(mysum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(mysum())
    print(mysum_bigger_than(10, 5, 20, 30, 6))
    print(mysum_bigger_than('g', 'a', 'z'))
    print(sum_numeric(10, 20, 'a', '30', 'bcd'))
    print(merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))
