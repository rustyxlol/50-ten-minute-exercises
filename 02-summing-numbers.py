"""
Reimplement the sum function
Thus, although you might invoke
sum([1,2,3]), you'd instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).

* ✅ The built-in version of sum takes an optional second argument, which is used as
the starting point for the summing. (That's why it takes a list of numbers as its
first argument, unlike our mysum implementation.) So sum([1,2,3], 4) returns
10, because 1+2+3 is 6, which would be added to the starting value of 4. 
Reimplement your mysum function such that it works in this way. 
If a second argument is not provided, then it should default to 0. 
Note that while you can write
a function in Python 3 that defines a parameter after *args, 
I'd suggest avoiding it and just taking two arguments—a list and an optional starting point.

* ✅ Write a function that takes a list of numbers. It should return the average (i.e.,
arithmetic mean) of those numbers

* ✅ Write a function that takes a list of words (strings). 
It should return a tuple containing three integers, 
representing the length of the shortest word, the length
of the longest word, and the average word length.

* ✅ Write a function that takes a list of Python objects. Sum the objects that either
are integers or can be turned into integers, ignoring the others. 
"""


from statistics import mean
import numbers


def mysum(*args):
    result = 0
    for i in args:
        result += i
    return result


def mysum_beyond(lst, starter=0):
    result = starter
    for i in lst:
        result += i
    return result


def myavg(lst):
    result = 0
    for i in lst:
        result += i
    return result/len(lst)


def wordstat(lst):
    minimum = 999
    maximum = 0
    total = 0

    for i in lst:
        if len(i) < minimum:
            minimum = len(i)
        if len(i) > maximum:
            maximum = len(i)
        total += len(i)

    return (minimum, total/len(lst), maximum)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def sum_all(lst):
    result = 0
    for i in lst:
        if isinstance(i, str):
            if i.isnumeric() or isfloat(i):
                result += float(i)
        if isinstance(i, numbers.Number):
            result += i

    return result


if __name__ == "__main__":
    print(mysum(1, 2, 3, 4, 5))

    lst = [1, 2, 3, 4, 5]
    words = ['hello', 'world', 'supercalifragilisticexpialidocuious']

    assert sum(lst, 5) == mysum_beyond(lst, 5)
    print(mysum_beyond([1, 2, 3, 4, 5], 5))

    assert mean([1, 2, 3, 4, 5]) == myavg([1, 2, 3, 4, 5])
    print(myavg([1, 2, 3, 4, 5]))

    assert wordstat(words) == (5, 15.0, 35)
    print(wordstat(words))

    print(sum_all([1, 2, 1.5, '3', 'a', 'b', '4.5', '2', 1]))
