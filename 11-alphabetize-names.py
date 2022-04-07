"""
write a function, alphabetize_names, that assumes the existence of a
PEOPLE constant defined as shown in the code. The function should return the list of
dicts, but sorted by last name and then by first name.


BEYOND THE EXERCISE
Given a sequence of positive and negative numbers, sort them by absolute value.

Given a list of strings, sort them according to how many vowels they contain.

Given a list of lists, with each list containing zero or more numbers, sort by the
sum of each inner list's numbers
"""
import pprint


def alphabetize_names(items):
    return sorted(items, key=lambda name: [name['last'], name['first']])


def abs_sort(items):
    return sorted(items, key=abs)


def vowel_size(word):
    return len([letter for letter in word.lower() if letter in 'aeiou'])
    # return sum([word.lower().count(vowel) for vowel in 'aeiou'])


def vowel_sort(items):
    return sorted(items, key=vowel_size)


def listlen_sort(items):
    return sorted(items, key=sum)


PEOPLE = [
    {
        'first': 'Reuven',
        'last': 'Lerner',
        'email': 'reuven@lerner.co.il'
    },
    {
        'first': 'Donald',
        'last': 'Trump',
        'email': 'president@whitehouse.gov'
    },
    {
        'first': 'Vladimir',
        'last': 'Putin',
        'email': 'president@kremvax.ru'
    }]


if __name__ == "__main__":
    pprint.pprint(PEOPLE)
    print("SORTED")
    pprint.pprint(alphabetize_names(PEOPLE))
    print(abs_sort([1, 2, -100, - 5, 1, 9, -10, 20, 30, 221]))
    print(vowel_sort(['aeio', 'axieom', 'abcd', 'abcde', 'jklsadjf', 'abcdi']))
    print(listlen_sort([[1, 2, 3], [100], [1, 2], [], [1, 4, 1, 2], [2]]))
