# to loop though an array, a name is assigned to the value
# which will equate our array item

# in this case language is an individual in the set of
# languages.

# this process will loop until the end of the array index

languages = ['python', 'javascript', 'html']

# colons are essential to represent what a function must do
# without a colon the code will return an error

# python
# javascript
# html
for language in languages:
    print(language)

# loops can be used to execute functions with arrays

# The code below will output:
# I can code in python!
# I cant wait to learn more Python!

# I can code in javascript!
# I cant wait to learn more Javascript!

# I can code in html!
# I cant wait to learn more Html!

# I wonder what I'll learn next?

for language in languages:
    print(f"I can code in {language}!")
    print(f"I cant wait to learn more {language.title()}!\n")

# python uses nesting/indentation rather than wrappers to
# execute functions meaning this print() will end the loop
# above.

print("I wonder what I'll learn next?")

# the range() will create a range of numbers between a set
# of numbers
numbers = list(range(1, 5))

print(numbers)

# a range can also skip numbers in a given range by passing 
# a third arguement, in this case start from 3
# skipping 2 until >=11

even_numbers = list(range(3, 11, 2))

# [3, 5, 7, 9]
print(even_numbers)

# by appending a range its data can be stored in an array
collection = []

# for the integer value of the index of range
for value in range(1, 11):
    # set item as value to the power of two
    item = value ** 2
    # append temporary item to collection to store results
    collection.append(item)

# this can be written as:
# for value in range(1, 11):
#   collection.append(value*2)
#
# print(collection)

print(collection)

# min(), max() and sum() can be useful functions
digits = [0, 3, 5, 2, 8]

# 0
print(min(digits))
# 8
print(max(digits))
# 18
print(sum(digits))

# list comprehensions combine looping with element
# creation in a single line

# squares will create append the current index to the second
# power between a range of 1 and 11
squares  = [value**2 for value in range(1, 11)]
print(squares)

# second example of a comprehension loop
twenty = [value+1 for value in range(0, 20)]
print(twenty)

# slicing a list is similar to the range function using a colon
# to define the beginning and end of the slice

sandwich = ['bread', 'meat', 'lettuce', 'mayo', 'bread']

print(sandwich[0:3])

# a slice can omit its first index by removing the modifier
print(sandwich[:3])

# the same applies in reverse
print(sandwich[3:])

# to output the last items in an array use `-i:` where i=value
print(sandwich[-3:])

# to loop through a slice
print("every sandwich needs")
for toppings in sandwich[1:3]:
    print(f'{toppings},')
print(f"and of coures {sandwich[0]}!")

# to copy a list into a new array a slice can be made that
# can omits the first and last indecies of the existing
# array

# appending lettuce to prove it is a unique array
super_sandwich = sandwich[:]
super_sandwich.append('lettuce')
print(sandwich)
print(super_sandwich)

# tuples are similar to lists. unlike lists however, are
# immutable. 

# the syntax of a touple is also similar to a list but rather
# than using square brackets as wrappers touples use
# parentheses.

touple = (1, 2)
print(touple[0])

# if generating a touple, ensure the touple contains a comma
# as what defines a touple is the presence of a comma

# example of single element touple:
single_touple = (1,)

# touples can be looped though the same as a standard list
# array
for content in touple:
    print(content)

# because a touple is an immutable element, it must be
# redefined in order to modify its' contents.
touple = (0, 1)
print(touple)