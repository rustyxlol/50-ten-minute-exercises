"""
write a Python function, format_sort_records, that takes the
PEOPLE list and returns a formatted string that looks like the following:
Trump   Donald      7.85
Putin   Vladimir    3.63
Xi      Jinping     10.60




✅ If you find tuples annoying because they use numeric indexes, you're not alone!
Reimplement this exercise using namedtuple objects (http://mng.bz/gyWl),
defined in the collections module. Many people like to use named tuples
because they give the right balance between readability and efficiency.


✅ Define a list of tuples, in which each tuple contains the name,
length (in minutes), and director of the movies nominated
for best picture Oscar awards last
year. Ask the user whether they want to sort the list by title,
length, or director's
name, and then present the list sorted by the user's choice of axis.

✅ Extend this exercise by allowing the user to sort by two or three of these fields,
not just one of them. The user can specify the fields by entering them separated
by commas; you can use str.split to turn them into a list.
"""

from collections import namedtuple
from operator import attrgetter

# PEOPLE = [('Donald', 'Trump', 7.85),
#           ('Vladimir', 'Putin', 3.626),
#           ('Jinping', 'Xi', 10.603)]

Person = namedtuple('Person', ['first', 'last', 'duration'])

Trump = Person('Donald', 'Trump', 7.85)
Vladimir = Person('Vladimir', 'Putin', 3.626)
Xi = Person('Xi', 'Jinping', 10.603)
Xia = Person('Xia', 'Jinpinga', 5.603)

PEOPLE = [Trump, Vladimir, Xi, Xia]


def format_sort_records(items, sort_key='first'):
    # template = "{1:10} {0:10} {2:5.2f}"
    try:
        output = []
        for item in sorted(items, key=attrgetter(*sort_key.split(','))):
            # output.append(template.format(*item))
            output.append(
                f"{item.first:10} {item.last:10} {item.duration:5.2f}")
        return output
    except AttributeError:
        print("No such attribute found")
        return None


def user_format():
    sort_key = input("Enter sort key(first, last, duration): ")
    try:
        print("\n".join(format_sort_records(PEOPLE, sort_key)))
    except TypeError:
        print("It's all a mess now")


if __name__ == "__main__":
    user_format()
