#  File: DayOfTheWeek.py
#  A program that uses an algorithm to display the day of the week of the date entered by the user.

def main():

    year = int(input("Please enter the year (an integer): "))
    month = str(input("Please enter the month (a string): "))
    day = int(input("Please enter the day (an integer): "))

    if month == "January":
        a = 11
    elif month == "February":
        a = 12
    elif month == "March":
        a = 1
    elif month == "April":
        a = 2
    elif month == "May":
        a = 3
    elif month == "June":
        a = 4
    elif month == "July":
        a = 5
    elif month == "August":
        a = 6
    elif month == "September":
        a = 7
    elif month == "October":
        a = 8
    elif month == "November":
        a = 9
    elif month == "December":
        a = 10

    b = day

    if a == 11 or a == 12:
        c = (year % 100) - 1
    else:
        c = year % 100

    if a == 11 or a == 12:
        d = (year - 1) // 100
    else:
        d = year // 100

    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r =  z % 7
    r = (r + 7) % 7

    if r == 0:
        weekday = "Sunday"
    if r == 1:
        weekday = "Monday"
    if r == 2:
        weekday = "Tuesday"
    if r == 3:
        weekday = "Wednesday"
    if r == 4:
        weekday = "Thursday"
    if r == 5:
        weekday = "Friday"
    if r == 6:
        weekday = "Saturday"

    print("The day of the week is " + str(weekday) + ".")

main()

