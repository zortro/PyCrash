# exzmple of what a list looks like:
consoles = ['nintendo', 'playstation', 'xbox']

print(consoles)

# fetching items by a negative index will fetch in the reverse
print(consoles[-2])
print(consoles[2])

message = f"My very first console was a {consoles[0].title()}"

print(message)

#  modifying index value by pointing to index
numbers = [1, 2, 3]
numbers[2] = 5
print(numbers)

# method: append() will append value to the end of a list
consoles.append('sega')

print(consoles)

# this can also be used to populate an empty list
shopping_cart = []
shopping_cart.append('tomatoes')
shopping_cart.append('lettuce')
shopping_cart.append('beef')

print(shopping_cart)

# the insert() method can be called to insert an element
# into a specific index of the list
shopping_cart.insert(2, 'buns')

print(shopping_cart)

# del statement is used to delete items from a list
del consoles[3]

print(consoles)

# tmethod: pop() will remove the last item in a list

last_console = consoles.pop()

# xbox
print(last_console)

# pop() specified indecies of a list
print(consoles.pop(0))

# method: remove() will remove a specified value from a list
# this method will only remove the first instance of a
# specified value
consoles.append('playstation 2')
old_console = 'playstation'

# playstation
consoles.remove(old_console)

# playstation 2
print(consoles)

alphabet = ['b', 'c', 'd', 'f', 'a', 'g', 'e']
# method: sort() will modify a list to alphebatize its contents
alphabet.sort()

print(alphabet)

# method: sorted() will temporarily alphebatize items in a list
cars = ['subaru', 'honda', 'toyota']

print(sorted(cars))

# method: reverse() will return a reversed copy of the parent list
cars.reverse()

print(cars)

# method: len() will return the number of items in a list
print(len(cars))