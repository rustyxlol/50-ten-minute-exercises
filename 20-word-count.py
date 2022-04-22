"""
The challenge for this exercise is to write a wordcount function that mimics the wc
Unix command. The function will take a filename as input and will print four lines
of output:
1 Number of characters (including whitespace)
2 Number of words (separated by whitespace)
3 Number of lines
4 Number of unique words (case sensitive, so “NO” is different from “no”)


✅ Ask the user to enter the name of a text file and then (on one line, separated by
spaces) words whose frequencies should be counted in that file. Count how
many times those words appear in a dict, using the user-entered words as the
keys and the counts as the values.

✅Create a dict in which the keys are the names of files on your system and the values
are the sizes of those files. To calculate the size, you can use os.stat
(http://mng.bz/dyyo).

✅Given a directory, read through each file and count the frequency of each letter. 
(Force letters to be lowercase, and ignore nonletter characters.) Use a dict
to keep track of the letter frequencies. What are the five most common letters
across all of these files
"""

import os
import pprint
from collections import Counter


def dir_analysis(path):
    letter_counts = Counter()
    for file in os.listdir(path):
        letter_counts = letter_counts + Counter(file.lower())
    pprint.pprint(letter_counts)


def list_dir():
    for file in os.listdir():
        print(file, os.stat(file).st_size, 'bytes')


def bte_custom_count():
    file_name = input("Enter file name: ")
    words = input("Enter words to count, split by space: ").split(' ')
    word_count = dict.fromkeys(words, 0)
    with open(file_name) as file:
        for line in file:
            for word in line.split():
                if word in word_count:
                    word_count[word] += 1
    print(word_count)


counts = {
    'letters': 0,
    'words': 0,
    'lines': 0,
    'uniques': 0,
}


def wordcount(file_name):
    unique_words = set()
    with open(file_name) as file:
        for line in file:
            counts['lines'] += 1
            counts['letters'] = len(line)
            counts['words'] = len(line.split())
            unique_words.update(line.split())
        counts['uniques'] = len(unique_words)

    print(counts)


if __name__ == "__main__":
    wordcount('random.txt')
    list_dir()
    dir_analysis('C:\\Users\\drdem\\Desktop\\Images')
    # bte_custom_count()
