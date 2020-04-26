# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
a = 1
value = 0
while(a == 1 or int(value) <= 0):
    value = input("What do you want to count to?")
    try:
        my_int = int(value)
        print(my_int)
        a = 0
    except:
        ValueError
i = 1

my_sum = 0
for i in range(1, int(value)+1):
    print(i, ' ')
    my_sum += i

if(int(value) <= 0):
    print("That is a negative number dummy")
print(my_sum)