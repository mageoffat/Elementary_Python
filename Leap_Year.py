# Write a program that prints the next 20 leap years.
from datetime import date
curr_year = date.today().year
START = 0
MAX = 20
curr_year = 1996
curr_year = (curr_year+3)//4*4

# for x in range(START, MAX):
#     if ((curr_year+4)%100 != 0):
#         curr_year = curr_year + 4
#         print (curr_year, " ", x+1)
#     else:
#         curr_year = curr_year + 8
#         print (curr_year, " ", x+1)

leapyears = []
SIZE = 20
while len(leapyears) < SIZE:
    if curr_year%400 == 0:
        leapyears.append(curr_year)
    elif curr_year%100 == 0:
        pass
    elif curr_year%4 == 0:
        leapyears.append(curr_year)
    curr_year+=4
print(leapyears)

