"""
* ✅ Write a function (guessing_game) that takes no arguments.
* ✅ When run, the function chooses a random integer between 0 and 100 (inclusive).
* ✅ Then ask the user to guess what number has been chosen
* ✅ Each time the user enters a guess, the program indicates one of the following
* - Too high
* - Too low
* - Just right
* ✅ If the user guesses correctly, the program exits. Otherwise, the user is asked to
* try again.
* ✅The program only exits after the user guesses correctly

BEYOND THE SCOPE

* ✅ Modify this program, such that it gives the user only three chances to guess the
correct number. If they try three times without success, the program tells them
that they didn’t guess in time and then exits.
* ✅ Not only should you choose a random number, but you should also choose a
random number base, from 2 to 16, in which the user should submit their
input. If the user inputs “10” as their guess, you’ll need to interpret it in the
correct number base; “10” might mean 10 (decimal), or 2 (binary), or 16
(hexadecimal).
* 🟨 Try the same thing, but have the program choose a random word from the dictionary,
and then ask the user to guess the word. (You might want to limit yourself to words
containing two to five letters, to avoid making it too horribly
difficult.) Instead of telling the user that they should guess a smaller or larger
number, have them choose an earlier or later word in the dict.
Partially covered this concept with bases dictionary.
"""

import pyinputplus as pyip
import random

bases = {
    bin: 2,
    oct: 8,
    int: 10,
    hex: 16
}


def guessing_game_bases():
    """Similar to guessing_game but with bases
    """
    randbase = random.choice(list(bases.keys()))
    randnum = str(randbase(random.randint(0, 100)))
    chances = 3

    while chances > 0:
        try:
            result = pyip.inputStr("\n\n\nEnter number: ", timeout=5)
            print(f"Chances remaining:{chances}")
            if int(randnum, bases[randbase]) > int(result, bases[randbase]):
                print("Too low")
            elif int(randnum, bases[randbase]) < int(result, bases[randbase]):
                print("Too high")
            else:
                print("Just right!")
                break
            chances -= 1

        except pyip.TimeoutException:
            chances -= 1
            print("Ran out of time there!")
            print(f"Chances remaining:{chances}")

        except ValueError:
            print(f"Seems like a different base! Hint: {bases[randbase]}")
            print(f"Chances remaining:{chances}")

    if chances == 0:
        print("Ran out of chances, sorry!")
        print(f"Base was : {bases[randbase]}, Number was : {randnum}")


def guessing_game():
    """Generates random number and asks for prediction 3 times
    """
    randnum = random.randint(0, 100)
    chances = 3

    while chances > 0:
        try:
            result = pyip.inputNum("\n\n\nEnter number: ", timeout=5)
            print(f"Chances remaining:{chances}")
            if randnum > result:
                print("Too low")
            elif randnum < result:
                print("Too high")
            else:
                print("Just right!")
                break
            chances -= 1

        except pyip.TimeoutException:
            chances -= 1
            print("Ran out of time there!")
            print(f"Chances remaining:{chances}")

    if chances == 0:
        print("\n\n\nRan out of chances, sorry!")
        print(f"Number was : {randnum}")


guessing_game_bases()
