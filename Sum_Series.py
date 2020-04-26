# Write a program that computes the sum of an alternating series
#  where each element of the series is an expression of the form ((-1)^{k+1})/(2 * k-1) 
# for each value of k from 1 to a million, multiplied by 4. Or, in more mathematical notation

START = 1
END = 1000000
summation = 0

for i in range(START, END):
    summation += ((-1)**(i+1))/(2*i-1)
print(4*summation)
