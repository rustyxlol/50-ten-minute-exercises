"""
In this exercise, write two functions. find_longest_word takes a filename as an
argument and returns the longest word found in the file. The second function, find-
_all_longest_words, takes a directory name and returns a dict in which the keys are
filenames and the values are the longest words from each file

Use the hashlib module in the Python standard library, and the md5 function
within it, to calculate the MD5 hash for the contents of every file in a userspecified directory. 
Then print all of the filenames and their MD5 hashes

Ask the user for a directory name. Show all of the files in the directory, as well
as how long ago the directory was modified. 

Open an HTTP server’s log file. (If you lack one, then you can read one from
me at http://mng.bz/vxxM.) Summarize how many requests resulted in numeric
response codes—202, 304, and so on.
"""


import hashlib
import os
from datetime import datetime


def bte_http_logs(file_name):
    response_codes = {}
    with open(file_name) as file:
        for line in file:
            data = line.split(' ')
            if data[8] in response_codes:
                response_codes[data[8]] += 1
            else:
                response_codes[data[8]] = 1
    print(response_codes)


def bte_recent_update(dir_name):
    files = os.listdir(dir_name)
    for file in files:
        print(file)
    print('last modified:', datetime.utcfromtimestamp(
        os.stat(dir_name).st_mtime).strftime('%Y-%m-%d %H:%M:%S'))


def bte_hashlib():
    files = os.listdir()
    for file in files:
        enc = hashlib.md5(file.encode('utf8'))
        print(f'{file:30} MD5 Hash:, {enc.digest()}')


def find_longest(file_name):
    with open(file_name, encoding='utf8') as file:
        print(sorted(file.read().split(), key=len)[-1])


def find_longest_dir(dir_name):
    for file_name in os.listdir(dir_name):
        find_longest(os.path.join(dir_name, file_name))


if __name__ == "__main__":
    find_longest('random.txt')
    find_longest_dir('C:\\Programming\\Python\\50-ten-minute-exercises\\books')
    bte_hashlib()
    bte_recent_update('C:\\Programming\\Python\\50-ten-minute-exercises')
    bte_http_logs('acces-log.txt')
