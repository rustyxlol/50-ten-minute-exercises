"""
write a function (called ubbi_dubbi) that takes a single
word (string) as an argument. It returns a string, the word's translation into Ubbi
Dubbi. So if the function is called with octopus, the function will return the string
uboctubopubus. And if the user passes the argument elephant, you'll output
ubelubephubant



BEYOND THE EXERCISE:
✅ Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn't), then the Ubbi Dubbi translation should be
similarly capitalized

✅ Remove author names—In academia, it's common to remove the authors' names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors' names, replace all names in the
article with _ characters

❕ URL-encode characters—In URLs, we often replace special and nonprintable
characters with a % followed by the character's ASCII value in hexadecimal. For
example, if a URL is to include a space character (ASCII 32, aka 0x20), we
replace it with %20. Given a string, URL-encode any character that isn't a letter
or number. For the purposes of this exercise, we'll assume that all characters
are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It
might help to know about the ord (http://mng.bz/EdnJ) and hex (http://mng
.bz/nPxg) functions.
Not sure if I understood this correctly.
"""


def ubbi_dubbi(word):
    result = ""
    for i in word:
        if i in "aeiou":
            result += "ub" + i
        elif i in "AEIOU":
            result += "UB" + i
        else:
            result += i
    return result


def remove_authors(paper):
    authors = paper.split('-')[1]
    for author in authors.split(','):
        paper = paper.replace(author, '_')
    return paper


def url_encode(url: str):
    result = ""
    if url.isascii():
        print("is ascii")
        return url

    for letter in url:
        if not letter.isascii():
            result += '%'+hex(ord(letter))[2:]
        else:
            result += letter
    return result


if __name__ == "__main__":
    assert "UBElubephubant" == ubbi_dubbi("Elephant")
    print(ubbi_dubbi("Elephant"))

    assert "uboctubopubus" == ubbi_dubbi("octopus")
    print(ubbi_dubbi("octopus"))

    print(remove_authors('Article Name - B. John, C. Bob, D. Alice'))

    print(url_encode("https://hello♥world.com"))
