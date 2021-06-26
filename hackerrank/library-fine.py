# problem-
# If the book is returned on or before the expected return date, no fine will be charged (i.e.: . return 0
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, . 15hacko * number of days
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the . 500hacko * number of days
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of . 10000

# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be .

# Sample Input

# 9 6 2015
# 6 6 2015
# Sample Output

# 45

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
            #if year of return is greater than year due
        return 10000
    elif m1>m2 and y1==y2:
            #if returned in the same year and month of return is greater than month due
        return (m1-m2)*500
    elif d1>d2 and y1==y2 and m1==m2:
        #if returned in the same year and month, and the date of return is greater than due date
        return (d1-d2)*15
    else:
        return 0

d1,m1,y1 = map(int,input().split())
d2,m2,y2 = map(int,input().split())
print(libraryFine(d1,m1,y1,d2,m2,y2))