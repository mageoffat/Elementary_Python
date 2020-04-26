# Write a program that prints a multiplication table for numbers up to 12.
# Tyra did this one with me

MAX = 12 #the highest integer, change this to get more times tables
START = 1 #starting times table integer


for i in range(START,MAX+1): # This will start from the START to the MAX and iterate with i
    for j in range(START,MAX+1): #This will start from the START to the MAX and iterate with j
        print(i*j,end="\t") # This will start with i = START, iterate through all j and then tab
    print() # this is a simple way to have an endline