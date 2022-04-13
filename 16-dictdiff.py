"""
Write a function dictdiff, that takes two dicts as arguments. The function returns
a new dict that expresses the difference between the two dicts


BEYOND THE EXERCISE
✅ The dict.update method merges two dicts. Write a function that takes any
number of dicts and returns a dict that reflects the combination of all of them.
If the same key appears in more than one dict, then the most recently merged
dict's value should appear in the output.


✅ Write a function that takes any even number of arguments and returns a dict
based on them. The even-indexed arguments become the dict keys, while the
odd-numbered arguments become the dict values. Thus, calling the function
with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being
returned.

✅ Write a function , dict_partition, that takes one dict (d) and a function (f) as
arguments. dict_partition will return two dicts, each containing key-value
pairs from d. The decision regarding where to put each of the key-value pairs
will be made according to the output from f, which will be run on each 
keyvalue pair in d. If f returns True, then the key-value pair will be put in the first
output dict. If f returns False, then the key-value pair will be put in the second
output dict. 
"""

from collections import defaultdict


def dictdiff(a, b):
    output = defaultdict(list)

    all_keys = a.keys() | b.keys()

    for key in all_keys:
        if a.get(key) != b.get(key):
            output[key].append(a.get(key))
            output[key].append(b.get(key))

    return output


def dictmerge(*dicts):
    output = {}
    for d in dicts:
        output.update(d)
    return output


def dictmake(*args):
    output = {}
    # All even indicies are keys
    # ('a', 1, 'b', 2)
    for index in range(len((args))):
        if index % 2 == 0:
            output[args[index]] = args[index + 1]
    return output


def dummyFunc(value):
    if value % 2 == 0:
        return True
    return False


def dict_partition(d, func):
    dict1 = {}
    dict2 = {}

    for key, value in d.items():
        if func(value):
            dict1[key] = value
        else:
            dict2[key] = value

    return dict1, dict2


if __name__ == "__main__":
    a = {'a': 1, 'b': 2, 'd': 3}
    b = {'a': 1, 'b': 2, 'c': 4}
    c = {'e': 4, 'f': 3, 'g': 5}
    d = {'x': 1, 'y': 2, 'c': 4}

    print(dictdiff(a, b))
    print(dictmerge(a, b, c, d))
    print(dictmake('a', 1, 'b', 2, 'c', 'k'))
    print(dict_partition(a, dummyFunc))
