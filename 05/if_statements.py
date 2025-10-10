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
full_cart
cart = ['apple', 'orange', 'mango', 'grape']