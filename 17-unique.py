"""
Count how many unique numebrs exist in a list
why is this even in exercise 17


✅ Read through a server (e.g., Apache or nginx) log file. What were the different
IP addresses that tried to access your server?

✅ Reading from that same server log, what response codes were returned to
users? The 200 code represents “OK,” but there are also 403, 404, and 500
errors. (Regular expressions aren't required here but will probably help.)

✅ Use os.listdir (http://mng.bz/YreB) to get the names of files in the current
directory. What file extensions (i.e., suffixes following the final . character)
appear in that directory? It'll probably be helpful to use os.path.splitext
(http://mng.bz/GV4v). 
"""

import os


def how_many_different_numbers(sequence):
    return len(set(sequence))


def apache_logs_bte():
    ips = set()
    status_codes = set()
    with open('apache_logs.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            details = line.split(' ')
            ip = details[0]
            code = details[8]

            ips.add(ip)
            status_codes.add(code)
    print("Status codes:", status_codes)
    return len(ips)


def files_in_curr_directory():
    all_files = os.listdir()
    extensions = set()
    for file in all_files:
        extensions.add(file.split('.')[1])
    print("Extensions:", extensions)


if __name__ == "__main__":
    print(how_many_different_numbers(
        [1, 1, 1, 1, 23, 3, 6, 4, 5, 2, 3, 3, 4, 1, 2]))
    print("Different IPs:", apache_logs_bte())
    files_in_curr_directory()
