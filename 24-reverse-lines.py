"""In many cases, we want to take a file in one format and save it to another format. In
this function, we do a basic version of this idea. The function takes two arguments: the
names of the input file (to be read from) and the output file (which will be created).
 For example, if a file looks like
abc def
ghi jkl
then the output file will be
fed cba
lkj ihg



BEYOND THE EXERCISE
✅ “Encrypt” a text file by turning all of its characters into their numeric equivalents 
(with the built-in ord function) and writing that file to disk. Now “decrypt”
the file (using the built-in chr function), turning the numbers back into their
original characters.

2 exercises omitted
"""

file_content = '''
abc def
ghi jkl
'''


def reversal():
    for word in file_content.split('\n'):
        print(word[::-1])


def encrypt():
    for letter in file_content:
        print(ord(letter), end=' ')


if __name__ == "__main__":
    reversal()
    encrypt()
