# Write a program that asks the user for a number n and gives
# them the possibility to choose between computing the sum and
# computing the product of 1,…,n.

a = 1
value = 0
while(a == 1):
    value = input("What do you want to count to?")
    try:
        my_int = int(value)
        print(my_int)
        a = 0
    except:
        ValueError

my_sum = 0
my_product = 1
sumproduct = input("if you want to sum the numbers enter 1, if you want to multiply the numbers enter 2")
while (not(sumproduct) != 1 or not(sumproduct) != 2):
    print("I hate you try again")
    sumproduct = input()

    

for i in range(1, int(value)+1):
    print(i, ' ')
    if(sumproduct == '1'):
        my_sum += i
    if(sumproduct == '2'):
        my_product *= i


if(int(value) <= 0):
    print("That is a negative number dummy")

if(sumproduct == '1'):
    print(my_sum)
if(sumproduct == '2'):
    print(my_product)
