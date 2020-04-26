# Modify the previous program such that only the users Alice and Bob are greeted with their names.
value = input("What is your name? \n")
N1 = 'Bob'
N2 = 'Alice'
if value == N1 or value == N2:
    print(f'Greetings {value}')
   
else: 
    print(f'You are not a valid user {value}')
    