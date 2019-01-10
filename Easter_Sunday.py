#  File: EasterSunday.py
#  A program that uses the Gaussian algorithm to compute the date of Easter Sunday for a specified year.

def main():

    print ("Enter year: ")
    y = int(input())

    # algorithmic values
    a = (y % 19)
    b = (y // 100)
    c = (y % 100)
    d = (b // 4)

    e = (b % 4)
    g = ( ((8 * b) + 13) // 25)
    h = ( (19 * a + b - d - g + 15) % 30)
    j = (c // 4)

    k = (c % 4)
    m = ( (a + 11 * h) // 319 )
    r = ( (2 * e + 2 * j - k - h + m + 32) % 7)

    n = ( (h - m + r + 90) // 25)        # month
    p = ( (h - m + r + n + 19) % 32)     # day

    print ("In " + str(y) + " Easter Sunday is on month " + str((n)) + " and day " + str((p)))

main()