"""
write a function (hex_output) that takes a hex number and returns the decimal equivalent. 
That is, if the user enters 50, you'll assume
that it's a hex number (equal to 0x50) and will print the value 80 to the screen. And
no, you shouldn't convert the number all at once using the int function, although it's
permissible to use int one digit at a time





BEYOND THE EXERCISE
🔰 (Already done) Reimplement the solution for this exercise such that it doesn’t use the int function at all, but rather uses the built-in ord and chr functions to identify the
character. This implementation should be more robust, ignoring characters
that aren’t legal for the entered number base

✅ Write a program that asks the user for their name and then produces a “name
triangle”: the first letter of their name, then the first two letters, then the first
three, and so forth, until the entire name is written on the final line.

"""
hex_map = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}


def hex_output(hex_number):
    result = 0
    for index, number in enumerate(hex_number):
        result = result + (hex_map[number] *
                           (16 ** (len(hex_number) - index - 1)))
    return result


def name_bte(name):
    for i in range(len(name) + 1):
        print(name[:i])


if __name__ == "__main__":
    print(hex_output('2A5'))
    name_bte('hehehuehue')
