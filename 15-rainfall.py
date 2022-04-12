"""
write a function, get_rainfall, that tracks rainfall in a number of cities. 
Users of your program will enter the name of a city; if the city name is blank, then
the function prints a report (which I'll describe) before exiting.
 If the city name isn't blank, then the program should also ask the user how much
rain has fallen in that city (typically measured in millimeters). After the user enters
the quantity of rain, the program again asks them for a city name, rainfall amount,
and so on—until the user presses Enter instead of typing the name of a city.
 When the user enters a blank city name, the program exits—but first, it reports
how much total rainfall there was in each city. Thus, if I enter
Boston
5
New York
7
Boston
5
[Enter; blank line]
the program should output
Boston: 10
New York: 7

BEYOND THE EXERCISE:
✅ Instead of printing just the total rainfall for each city, print the total rainfall and
the average rainfall for reported days. Thus, if you were to enter 30, 20, and 40
for Boston, you would see that the total was 90 and the average was 30.

✅ Open a log file from a Unix/Linux system—for example, one from the Apache
server. For each response code (i.e., three-digit code indicating the HTTP
request's success or failure), store a list of IP addresses that generated that code

❗ did a very similar one previously, very similar to how the above one works.
Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results.

"""
from collections import defaultdict

WEATHER_CITY = dict()
WEATHER_COUNTS = dict()
# LOG_FILE = dict()
LOG_FILE = defaultdict(list)


def get_rainfall():
    while True:

        city = input("Enter city: ")
        if not city:
            break
        temperature = float(input("Enter temperature: "))
        if not temperature:
            print("No temp found, exiting")
            break

        WEATHER_CITY[city] = WEATHER_CITY.get(city, 0) + temperature
        WEATHER_COUNTS[city] = WEATHER_COUNTS.get(city, 0) + 1

    for key, value in WEATHER_CITY.items():
        print(key)
        print("Total = ", value)
        print("Average = ", value / WEATHER_COUNTS[key])


def log_file_bte():
    with open('apache_logs.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            details = line.split(' ')
            ip = details[0]
            stat_code = details[8]
            # ALT
            # LOG_FILE.setdefault(stat_code, []).append(ip)
            LOG_FILE[stat_code].append(ip)

    print(LOG_FILE['404'])


if __name__ == "__main__":
    # get_rainfall()
    log_file_bte()
