# a list is a set of items contained in square brackets
# `[]`

consoles = ['nintendo', 'playstation', 'xbox']

# ['nintendo', 'playstation', 'xbox']
print(consoles)

# xbox
# note: when accessing items based on indecies the
# returned value is not contained in brackets.
# using an index value of -1 will fetch the last element
# in the array given there are elements in the array
print(consoles[2])

# example use of index value
message = f"My very first console was a {consoles[0].title()}"

# My very first console was a Nintendo
print(message)

# example of an index value can be modified
numbers = [1, 2, 3]
numbers[2] = 5
print(numbers)

# the append() method can be used to add elements
# to the end of a list
consoles.append('sega')

#['nintendo', 'playstation', 'xbox', 'sega']
print(consoles)

# this can also be used to populate an empty array
shopping_cart = []
shopping_cart.append('tomatoes')
shopping_cart.append('lettuce')
shopping_cart.append('beef')

# ['tomatoes', 'lettuce', 'beef']
print(shopping_cart)

# the insert() method can be called to insert an element
# into a specific index of the list

shopping_cart.insert(2, 'buns')

# ['tomatoes', 'lettuce', 'buns', 'beef']
print(shopping_cart)

# to remove elements from a list the del statement can
# be called to remove said element.
del consoles[3]

# ['nintendo', 'playstation', 'xbox']
print(consoles)

# the method pop() can be called to remove the last
# element in an array

last_console = consoles.pop()

# xbox
print(last_console)

# pop() can be used in combination with an index number
# to pop a specific index element out of it's array

# nintendo
print(consoles.pop(0))

# the remove() method can also be used to remove a given
# value in an array

# remove() will only remove the first instance of a
# specified value

consoles.append('playstation 2')
old_console = 'playstation'

# playstation
consoles.remove(old_console)

# notice using pop() or remove() on these elements will
# remove them from their respective array

# playstation 2
print(consoles)

alphabet = ['b', 'c', 'd', 'f', 'a', 'g', 'e']

# the sort() method can be called to sort lists
# alphabetically, this will affect the array
# permenantly

alphabet.sort()

# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(alphabet)

# lists can be temporarily sorted by printing the array
# using the sorted() method
cars = ['subaru', 'honda', 'toyota']

# ['honda', 'subaru', 'toyota']
print(sorted(cars))

# lists can be reversed using the reverse() method
cars.reverse()

# ['toyota', 'honda', 'subaru']
print(cars)

# to get the index length of the array use the len()
# method

# 3
print(len(cars))