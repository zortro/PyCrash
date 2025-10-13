# To utilize conditionals in python it is similar to other
# languages

list = [1, 2, 3, 4]

# it is important to keep in mind the usage of colons to
# execute code contained in the statement.
for item in list:
    if item == 2:
        print('two')
    else:
        print(item)

# when checking equality with string values, remember that
# capital and lower case characters are going to be
# returned as inequivelant values

# when contrasting inequalities use `!=`
for item in list:
    if item != 2:
        print('not 2')
    else:
        print(item)

# mathematical conditions can also be applied
# <
# >
# <=
# >=
for item in list:
    if item >= 2:
        print('>=2')
    else:
        print('<2')

# to check if a value is in a list declare a value to look
# for then use the modifier `in` to check the list
if 4 in list:
    print(4)

# to check if a value is not in a list declare a value to
# look for then use the modifier `not in` to check the list
if 5 not in list:
    print('did not find 5')

# boolean expressions are very useful in conditionals
# note the bool value requires capitalization to be used
identity = 'Niko'

if identity == 'Niko':
    print('Hello Niko')
identity = 'Roman'
if identity != 'Niko':
    print("You're not Niko!")

# for an `if-else` chain in Python use `elif`

num = [1, 50, 100]
for digit in num:
    if digit > 50:
        print(f'{digit} > 50')
    elif digit == 50:
        print(f'{digit} == 50')
    elif digit < 50:
        print(f'{digit} < 50')

# because only a single variable in the list is <100 the
# code can be written as follows:
# for digit in num:
#    if digit > 50:
#        print(f'{digit} > 50')
#    elif digit == 50:
#        print(f'{digit} == 50')
#    else:
#        print(f'{digit} < 50')

# an appropriate usage of the elif chain is to use only when
# a single test needs to be passed

# notice how toppings checked for past bacon will not be
# recognized, this is because it finds the first result in
# the logical order of the program and returns the results
# for the specific result.
# a loop would be more appropriate for this scenario.
sandwich_toppings = ['bacon', 'lettuce', 'tomato']

if 'bacon' in sandwich_toppings:
    print('adding mayo')
    sandwich_toppings.append('mayo')
elif 'lettuce' in sandwich_toppings:
    print('adding mustard')
elif 'tomato' in sandwich_toppings:
    print('adding salt')

# the code below takes an order and checks for tomato. if
# tomatoes are ordered they will not be appended to the order
# list.
order = []
    
for topping in sandwich_toppings:
    if topping == 'tomato':
        print("Sorry, we're all out of tomatoes.")
    else:
        print(f'{topping}? You got it!')
        order.append(topping)
print(f'One sandwich with:')

for items in order:
    print(items)
print('coming right up!')

# assume the order list remains empty
order = []

# the code first checks for an order then for any items will
# print to terminal. If there are no items the code will 
# print the else statement to the terminal.
if order:
    for items in order:
        print(f'{items}, you got it!')
    print('\nAnything else?')
else:
    print('Just the bun? Are you sure?')
    
# Now add an imaginary menu. 
# Note the usage of a touple
menu = ('bacon', 'lettuce', 'tomato', 'mushroom')
order = ['bacon', 'lettuce', 'tomato', 'mustard']

# the code below takes each item in the order list and for each
# item that is found in the menu list the console prints
# the item in question. if the item is not found the console
# will print a message appologizing for not containing such item.
for item in order:
    if item in menu:
        print(f'{item}, gotcha.')
    else:
        print(f'sorry, we dont have {item}')
print('Can I get you anything else?')

