"""
writing a function, strsort, that takes a
single string as its input and returns a string. The returned string should contain the
same characters as the input, except that its characters should be sorted in order, from
the lowest Unicode value to the highest Unicode value. For example, the result of
invoking strsort('cba') will be the string abc

BEYOND THE EXERCISE

Given the string “Tom Dick Harry,” break it into individual words, and then sort
those words alphabetically. Once they’re sorted, print them with commas (,)
between the names.

Which is the last word, alphabetically, in a text file?

Which is the longest word in a text file
"""


def strsort(string):
    return "".join(sorted(string))


def strssort(string):
    return ",".join(sorted(["".join(sorted(name)) for name in string.split()]))


def last_word():
    with open('random.txt') as f:
        data = f.read()
        print(data.split()[-1])


def longest_word():
    with open('random.txt') as f:
        data = f.read()
        max_length = len(max(data.split(), key=len))
        [print(word) for word in data.split() if len(word) == max_length]


if __name__ == "__main__":
    print("strsort: ", strsort("cba"))
    print("strssort: ", strssort("Tom Dick Harry"))
    print("Last word in the text file:", end="")
    last_word()
    print("Longest word in the text file:")
    longest_word()
