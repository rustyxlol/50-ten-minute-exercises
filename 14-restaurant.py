"""
Create a new constant dict, called MENU, representing
the possible items you can order at a restaurant. The keys will be strings, 
and the values will be prices (i.e., integers). You should then write a function, restaurant, that
asks the user to enter an order:
* If the user enters the name of a dish on the menu, the program prints the price
and the running total. It then asks the user again for their order.
* If the user enters the name of a dish not on the menu, the program scolds the
user (mildly). It then asks the user again for their order.
* If the user enters an empty string, the program stops prompting and prints the
total amount
Example
Order: sandwich
sandwich costs 10, total is 10
Order: tea
tea costs 7, total is 17
Order: elephant
Sorry, we are fresh out of elephant today.
Order: <enter>
Your total is 17



BEYOND THE EXERCISE:
✅ Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user must
enter a username and password. If there is a match, then indicate that the user
has successfully logged in. If not, then refuse them entry. (Note: This is a nice
little exercise, but please never store unencrypted passwords. It’s a major security risk.)


✅ Define a dict whose keys are dates (represented by strings) from the most recent
week and whose values are temperatures. Ask the user to enter a date, 
and display the temperature on that date, as well as the previous and subsequent dates,
if available.

✅ Define a dict whose keys are names of people in your family, and whose values
are their birth dates, as represented by Python date objects (http://mng.bz/
jggr). Ask the user to enter the name of someone in your family, and have the
program calculate how many days old that person is
"""

import datetime


DATE_TEMPS = {
    '1/2/3': 20,
    '2/2/3': 30,
    '3/2/3': 50,
    '4/2/3': 20,
}

USER_LOGINS = {
    'admin': 'admin',
    'user1': 'insecurePassword'
}

MENU = {
    'sandwich': 10,
    'boorger': 20,
    'hamboorger': 987,
}

AGES = {
    'abc': datetime.date(2007, 10, 10),
    'xyz': datetime.date(2000, 11, 10)
}


def restaurant():
    total = 0
    while True:
        order = input("Order: ")
        if not order:
            break
        if order in MENU:
            total += MENU[order]
            print(f"{order} costs {MENU[order]}, total is: {total}")
        else:
            print(f"We are out of {order}")
    print("Your total is: ", total)


def login_auth():
    while True:
        username = input("Enter username: ")
        if username in USER_LOGINS:
            password = input("Enter password: ")
            if USER_LOGINS[username] == password:
                print("Welcome to the club")
                return
            print("Wrong password entered :(")
        else:
            print("That username does not exist")


def date_temps():
    while True:
        date = input("Enter date: ")
        if date in DATE_TEMPS:
            print(f"THE TEMP ON {date} WAS: {DATE_TEMPS[date]}")
            for dt in sorted(DATE_TEMPS):
                print(f"DAY: {dt:10} TEMP:{DATE_TEMPS[dt]}")
            return
        print("NO DATE FOUND")


def age_calculator():
    while True:
        person = input("Enter name: ")
        if person in AGES:
            print(
                f"{person}, born on {AGES[person]} is {(datetime.date.today() - AGES[person]).days} days old today")
            return
        print("Person not found!")


if __name__ == "__main__":
    restaurant()
    login_auth()
    date_temps()
    age_calculator()
