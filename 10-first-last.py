"""
Write a function, firstlast, that takes
a sequence (string, list, or tuple) and returns the first and last elements of that
sequence, in a two-element sequence of the same type. So firstlast('abc') will
return the string ac, while firstlast([1,2,3,4]) will return the list [1,4].




BEYOND THE EXERCISE
✅ Write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of
the odd-indexed numbers. So calling the function as even_odd_sums([10, 20,
30, 40, 50, 60]), you'll get back [90, 120].

✅ Write a function that takes a list or tuple of numbers.
Return the result of alternately adding and subtracting numbers from each other.
So calling the function as plus_minus([10, 20, 30, 40, 50, 60]),
you'll get back the result of 10+20-30+40-50+60, or 50

✅ Write a function that partly emulates the built-in zip function (http://mng.bz/
Jyzv), taking any number of iterables and returning a list of tuples. Each tuple
will contain one element from each of the iterables passed to the function.
Thus, if I call myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20,
'b'), (30, 'c')]. You can return a list (not an iterator) and can assume that all
of the iterables are of the same length
"""


def firstlast(arg):
    return arg[:1] + arg[-1:]


def even_odd_sums(sequence):
    evens = sum(sequence[0::2])
    odds = sum(sequence[1::2])
    return [evens, odds]


def plus_minus(sequence):
    return sum(sequence[1::2]) - sum(sequence[2::2]) + sequence[0]


def myzip(iter1, iter2):
    return [(iter1[i], iter2[i]) for i in range(len(iter1))]


if __name__ == "__main__":
    print(firstlast("abc"))
    print(firstlast([1, 2, 3, 4]))
    print(even_odd_sums([10, 20, 30, 40, 50, 60]))
    print(plus_minus([10, 20, 30, 40, 50, 60]))
    print(myzip([10, 20, 30], 'abc'))
