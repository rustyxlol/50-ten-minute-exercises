"""
In this exercise, write a function, passwd_to_dict, that reads from a Unix-style
“password file,” commonly stored as /etc/passwd, and returns a dict based on it

🟨 Did the actual exercise very similar to this
Read through /etc/passwd, creating a dict in which user login shells (the final
field on each line) are the keys. Each value will be a list of the users for whom
that shell is defined as their login shell.

✅ Ask the user to enter integers, separated by spaces. From this input, create a
dict whose keys are the factors for each number, and the values are lists containing those 
of the users' integers that are multiples of those factors.

✅ From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell.
"""

from collections import defaultdict
from pprint import pprint


user_dict = {}
number_factors = defaultdict(list)
UNKeys = defaultdict(dict)


def BTE_UNKeys(file_name):
    with open(file_name) as file:
        for line in file:
            if line.startswith(('#', '\n')):
                continue
            user_info = line.split(':')
            user_dict[user_info[0]] = {
                'id': user_info[2],
                'role': user_info[7],
            }
    pprint(user_dict)


def find_factors(x):
    return [i for i in range(1, x+1) if x % i == 0]


def BTE_int():
    user_input = input("Enter integers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    factors = []

    for number in numbers:
        factors = find_factors(number)
        for fact in factors:
            number_factors[fact].append(number)

    pprint(number_factors)


def passwd_to_dict(file_name):
    with open(file_name) as file:
        for line in file:
            if line.startswith(('#', '\n')):
                continue
            user_info = line.split(':')
            user_dict[user_info[0]] = [user_info[2], user_info[7]]
    print(user_dict)


if __name__ == "__main__":
    passwd_to_dict('etc-pass')
    BTE_UNKeys('etc-pass')
    BTE_int()
