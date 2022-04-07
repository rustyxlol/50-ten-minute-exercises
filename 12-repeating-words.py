"""
Write a function, most_repeating_word, that takes a sequence of strings as input. The
function should return the string that contains the greatest number of repeated letters. In other words
* For each word, find the letter that appears the most times.
* Find the word whose most-repeated letter appears more than any other.
That is, if words is set to
words = ['this', 'is', 'an', 'elementary', 'test', 'example']
then your function should return elementary. That’s because
* this has no repeating letters.
* is has no repeating letters.
* an has no repeating letters.
* elementary has one repeating letter, e, which appears three times.
* test has one repeating letter, t, which appears twice.
* example has one repeating letter, e, which appears twice.



BEYOND THE EXERCISE
✅ Instead of finding the word with the greatest number of repeated letters, find
the word with the greatest number of repeated vowels.

❌ Write a program to read /etc/passwd on a Unix computer. The first field contains
the username, and the final field contains the user’s shell, 
the command interpreter. Display the shells in decreasing order of 
popularity, such that the most popular shell is shown first, the second most popular shell second, and so forth.

❌ For an added challenge, after displaying each shell, also show the usernames
(sorted alphabetically) who use each of those shells. 

"""
from collections import Counter

words = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating(items):
    return max(items, key=most_repeating_letter)


def most_repeating_vowels(word):
    return Counter(v for v in word.lower() if v in 'aeiou').most_common(1)[0][1]


def most_repeating_bte(items):
    return max(items, key=most_repeating_vowels)


if __name__ == "__main__":
    print(most_repeating(words))
    print(most_repeating_bte(words))
