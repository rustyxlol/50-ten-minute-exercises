"""
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until
the user presses Enter. At that point, the function exits—but only after calculating and
displaying the total time that the 10 km runs took.
For example, here’s what the output would look like if the user entered three data
points:
Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 10
Enter 10 km run time: <enter>
total of 15.0, over 3 runs


BEYOND THE EXERCISE
✅ Write a function that takes a float and two integers (before and after). The
function should return a float consisting of before digits before the decimal
point and after digits after. Thus, if we call the function with 1234.5678, 2 and
3, the return value should be 34.567.



✅ Explore the Decimal class (http://mng.bz/oPVr), which has an alternative
floating-point representation that’s as accurate as any decimal number can be.
Write a function that takes two strings from the user, turns them into decimal
instances, and then prints the floating-point sum of the user’s two inputs. In
other words, make it possible for the user to enter 0.1 and 0.2, and for us to get
0.3 back
"""
import math
from decimal import *


def run_timing():
    total_time = 0
    runs = 0
    while True:
        run_time = input("Enter 10 km run time: ")
        if not run_time:
            break
        try:
            total_time += float(run_time)
            runs += 1
        except ValueError:
            print("Please enter a proper value")
    return f'total of {total_time/runs}, over {runs} runs'


def float_cutter(value, before, after):
    # BTE 1
    # before_dot = str(math.trunc(value % (before * 100)))
    # after_dot = str(math.trunc((value % 1) * 10**after))
    # return float(before_dot+'.'+after_dot)

    new_value = str(value).split('.')
    return float(".".join((new_value[0][-before:], new_value[1][:after])))


def sum_floats():
    # BTE 2
    str1 = input("Enter number 1: ")
    str2 = input("Enter number 2: ")
    print(Decimal(str1) + Decimal(str2))


if __name__ == "__main__":
    print(run_timing())

    print(float_cutter(1234.5678, 2, 3))

    sum_floats()
