# Modify the previous program such that only multiples of three or five
#  are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
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
i = 1
my_sum = 0
for i in range(1, int(value)+1):
    if i%3 == 0:
        print(i, ' ')
        my_sum += i
    elif i%5 == 0:
        print(i, ' ')
        my_sum += i

if(int(value) <= 0):
    print("That is a negative number dummy")
print(my_sum)