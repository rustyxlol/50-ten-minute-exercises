"""
Pig latin but for sentences

BEYOND THE EXERCISE

✅ Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number.

✅ Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a
way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].

✅ Read through an Apache logfile. If there is a 404 error—you can just search for
' 404 ', if you want—display the IP address, which should be the first element
LOGFILE FROM: https://github.com/elastic/examples/tree/master/Common%20Data%20Formats/apache_logs
"""
from string import punctuation


def isVowel(letter):
    if letter in 'aeiou' or letter in 'AEIOU':
        return True
    return False


def pig_latin(sentence):
    result = []
    for word in sentence.split(' '):
        if isVowel(word[0]):
            result.append(word + 'way')
        else:
            result.append(word[1:] + word[0] + 'ay')

    return " ".join(result)


def nonsensical_sentence():
    with open('random.txt') as f:
        data = f.read()
        data = data.splitlines()
        for i in range(10):
            print(data[i].split()[i], end=" ", sep=" ")


def transposer(lst):
    templist = []
    result = []
    for i in lst:
        templist.append(i.split())

    for i in range(len(lst)):
        temptrans = []
        for j in range(len(lst)):
            temptrans.append(templist[j][i])
        result.append(" ".join(temptrans))
    print(result)


def apache_log():
    with open('apache_logs.txt') as f:
        data = f.read()
        for i in data.splitlines():
            if "404" in i:
                print("BAD IP =", i.split(' ')[0])


if __name__ == "__main__":
    text = "this is a test translation"
    # print(pig_latin(text))
    # nonsensical_sentence()
    # transposer(['abc def ghi',
    #             'jkl mno pqr',
    #             'stu vwx yz'])
    apache_log()
