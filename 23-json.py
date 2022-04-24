"""
Your function should print the highest, lowest, and average test scores for each subject
in each class. Given two files (9a.json and 9b.json) in the scores directory, we would
see the following output:
scores/9a.json
science: min 75, max 97, average 86.4
literature: min 78, max 98, average 83.6
math: min 65, max 100, average 85.0
scores/9b.json
science: min 35, max 95, average 82.0
literature: min 38, max 98, average 7


✅ Convert /etc/passwd from a CSV-style file into a JSON-formatted file. The
JSON file will contain the equivalent of a list of Python tuples, with each tuple
representing one line from the file.

🟨same as above?
For a slightly different challenge, turn each line in the file into a Python dict.
This will require identifying each field with a unique column or key name. If
you’re not sure what each field in /etc/passwd does, you can give it an arbitrary name.

✅ Ask the user for the name of a directory. Iterate through each file in that directory (ignoring subdirectories), getting (via os.stat) the size of the file and
when it was last modified. Create a JSON-formatted file on disk listing each filename, size, and modification timestamp. Then read the file back in, and identify which files were modified most and least recently, and which files are largest
and smallest, in that directory. 
"""
import csv
import json
import os
from datetime import datetime

from collections import defaultdict
from statistics import mean


def bte_recent_update(dir_name):
    json_doc = []
    files = os.listdir(dir_name)
    for file in files:
        print(file)
        json_doc.append({
            'file_name': file,
            'size': os.stat(file).st_size,
            'last_modified': datetime.utcfromtimestamp(
                os.stat(os.path.join(dir_name, file)).st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        })

    for file in sorted(json_doc, key=lambda d: d['last_modified']):
        print(file)


def bte_csv_to_json():
    json_doc = []
    with open('pass.csv') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                continue
            name, pass1, pass2 = row
            user = {
                'name': name,
                'pass1': pass1,
                'pass2': 'pass2'
            }
            json_doc.append(user)
    print(json_doc)


def hlajson():
    scores = defaultdict(list)
    with open('scores/9a.json') as file:
        data = json.load(file)
        for elem in data:
            for key, value in elem.items():
                scores[key].append(value)

    for key, values in scores.items():
        print(
            f"{key}: min {min(values)}, max {max(values)}, average {mean(values)}")


if __name__ == "__main__":
    # hlajson()
    # bte_csv_to_json()
    bte_recent_update('C:\\Programming\\Python\\50-ten-minute-exercises')
