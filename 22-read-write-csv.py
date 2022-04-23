"""
For this exercise, create a function, passwd_to_csv, that takes two filenames as
arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
 The new file's contents are the username (index 0) and the user ID (index 2).
Note that a record may contain a comment, in which case it will not have anything at
index 2; you should take that into consideration when writing the file. The output file
should use TAB characters to separate the elements.
 Thus, the input will look like this
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
# I am a comment line
_ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
and the output will look like this:
root 0
daemon 1
_ftp 98


 Extend this exercise by asking the user to enter a space-separated list of integers,
indicating which fields should be written to the output CSV file. Also ask
the user which character should be used as a delimiter in the output file. Then
read from /etc/passwd, writing the user's chosen fields, separated by the user's
chosen delimiter.

 Write a function that writes a dict to a CSV file. Each line in the CSV file should
contain three fields: (1) the key, which we'll assume to be a string, (2) the value,
and (3) the type of the value (e.g., str or int).

 Create a CSV file, in which each line contains 10 random integers between 10
and 100. Now read the file back, and print the sum and mean of the numbers
on each line.
"""

import csv
import random

RANDOM_DICT = {
    'someKey': 'a value',
    'AnotherKey': 'another value',
}


def bte_random():
    with open('e22random.csv', 'w', encoding='utf8') as outf:
        csv_writer = csv.writer(outf)
        for _ in range(100):
            csv_writer.writerow([random.randint(10, 100) for i in range(10)])

    with open('e22random.csv', encoding='utf8') as inf:
        csv_reader = csv.reader(inf)
        for row in csv_reader:
            if not row:
                continue
            numbers = [int(num) for num in row]
            print('Sum:', sum(numbers))
            print('Average:', sum(numbers)/len(numbers))


def dict_to_csv():
    with open('e22dtocsv.csv', 'w', encoding='utf8') as outf:
        csv_writer = csv.writer(outf)
        for key, value in RANDOM_DICT.items():
            csv_writer.writerow([key, value, type(value).__name__])
            print([key, value, type(value).__name__])


def passwd_to_csv(infile, outfile):
    fields = input("Enter fields, separated by space: ")
    fields = [int(field) for field in fields.split(' ')]

    delim = input("Enter delimiter: ")

    with open(infile, encoding='utf8') as inf:
        with open(outfile, 'w', encoding='utf8') as outf:
            csv_writer = csv.writer(outf)
            for line in inf:
                data = line.split(delim)
                print([data[x] for x in fields])
                csv_writer.writerow([data[x] for x in fields])


if __name__ == "__main__":
    # passwd_to_csv('etc-pass', 'pass.csv')
    # dict_to_csv()
    bte_random()
