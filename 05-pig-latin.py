"""

If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway

If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”

For this exercise, write a Python function (pig_latin) that takes a string as input,
assumed to be an English word. The function should return the translation of this word
into Pig Latin. You may assume that the word contains no capital letters or punctuation.



BEYOND THE EXERCISE

✅ Handle capitalized words—If a word is capitalized 
(i.e., the first letter is capitalized, but the rest of the word isn't), 
then the Pig Latin translation should be
similarly capitalized.

✅ Handle punctuation—If a word ends with punctuation, then that punctuation
should be shifted to the end of the translated word.

Consider an alternative version of Pig Latin—We don't check to see if the first letter
is a vowel, but, rather, we check to see if the word contains two different vowels.
If it does, we don't move the first letter to the end. Because the word “wine”
contains two different vowels (“i” and “e”), we'll add “way” to the end of it, giving us “wineway.” By contrast, the word “wind” contains only one vowel, so we
would move the first letter to the end and add “ay,” rendering it “indway.” How
would you check for two different vowels in the word? (Hint: sets can come in
handy here.)
"""

from string import punctuation


def checkVowel(letter):
    if letter in 'aeiou' or letter in 'AEIOU':
        return True
    return False


def pig_latin(word):
    if word[-1] in punctuation:
        if checkVowel(word[0]):
            return word[:-1] + 'way' + word[-1]
        return word[1:-1] + word[0] + 'ay' + word[-1]

    if checkVowel(word[0]):
        return word + 'way'
    return word[1:] + word[0] + 'ay'


if __name__ == "__main__":
    print(pig_latin("Air,"))
    print(pig_latin("Python,"))
    print(pig_latin("computer"))
