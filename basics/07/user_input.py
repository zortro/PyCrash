# taking input can be done using the input() funciton
msg = input('enter something: ')

first = input('what is your first name? ')

prompt = 'If you wish you may share your last name.'
# to follow up a prompt instead of value = prompt(), use
prompt += '\nWhat is your last name? '

last = input(prompt)

# the input value can be returned by calling upon it
print(f'hello {first} {last}')

# when taking numerical input it will by default be
# stored as a string.
age = input('how old are you? ')

# handles lack of input to allow code to continue
if age == '':
    age = '0'
    
# to compare numerical values the input value can be
# converted to an integer using int()
age = int(age)

if age <= 12:
    print(f'{age}: child')
elif age <= 18:
    print(f'{age}: teen')
else:
    print(f'{age}: adult')
    
# the modulo operator divides one number by another and
# returns the remainder
# 1
print(4 % 3)
# 2
print(10 % 7)
# 0
print(8 % 4)

num = input('check if number is even or odd: ')

if num == '':
    num = 0

num = int(num)

if num % 2 == 0:
    print('even')
else:
    print('odd')
    
