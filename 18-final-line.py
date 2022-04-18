"""
write a function (get_final_line) that takes a filename as an
argument. The function should return that file's final line on the screen.



BEYOND THE EXERCISE

✅ Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace
surrounded by whitespace) that contain only integers, and sum them.

✅ Create a text file (using an editor, not necessarily Python) containing two tabseparated 
columns, with each column containing a number. Then use Python
to read through the file you've created. For each line, 
multiply each first number by the second, and then sum the results from all the lines. 
Ignore any line that doesn't contain two numeric columns.

✅ Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.
"""


def count_vowels(file_name):
    vowels = 'aeiou'
    vowels_dict = {}.fromkeys(vowels, 0)

    with open(file_name) as file:
        for word in file.read():
            for letter in word:
                if letter in vowels:
                    vowels_dict[letter] += 1
    return vowels_dict


def get_colsum(file_name):
    total = 0
    with open(file_name) as file:
        for line in file:
            product = 1
            if len(line.split()) == 2:
                for number in line.split():
                    if number.isnumeric():
                        product = product * int(number)
            total += product
    return total


def get_sum(file_name):
    total = 0
    with open(file_name) as file:
        for line in file:
            for word in line.split(' '):
                if word.isnumeric():
                    total += int(word)
    return total


def get_final_line(file_name):
    with open(file_name) as file:
        return file.readlines()[-1]


if __name__ == "__main__":
    # print(get_final_line('random.txt'))
    # print(get_sum('random.txt'))
    # print(get_colsum('18-test.txt'))
    print(count_vowels('random.txt'))
