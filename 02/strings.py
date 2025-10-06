# this time use `message` as a variable containing
# what terminal output

# output "Hello Python, this message is contained in a variable!"
message = "Hello Python, this message is contained in a variable!"
print(message)

# using the method title() on our name variable will call for the
# first character in each word to title case, a capitalized letter.

# output "John Doe"
name = "john doe"
print(name.title())

# output "JOHN DOE"
print(name.upper())

# output "john doe"
# note because variable is already lower output is expected to
# remain the same as input
print(name.lower())

first = "johnny"
last = "doe"

# utilizing an f string will join variables first and last to create a new
# variable holding full name.
full = f"{first} {last}"

# output "johnny doe"
print(full)

# using f strings in combination with the title method
# output "Hello, Johnny Doe. Welcome to Python!"
print(f"Hello, {first.title()} {last.title()}. Welcome to Python!")

# containing an f string in a variable
second_message = f"Greetings {first.title()} {last.title()}. I am... {name.upper()}!!"

# output "Greetings Johnny Doe. I am... JOHN DOE!!"
print(second_message)

#using `\t` to tab text in output

# output "    Python!"
print("\tPython!")

# using `\n` to create a new line in output

# output
# "
# Languages:
# Python
# Javascript
# "
print("Languages:\nPython\nJavaScript")

# using the rstrip() method, whitespace at the end of a string can be removed
# to python whitespace is distinguishable to the program. Meaning 'Python'
# and 'Python ' are two seperate values.

whitespace = 'Python '

#output "example with whitespace Python !"
print(f"example with whitespace {whitespace}!")

# output "example without whitespace Python!"
print(f"example without whitespace {whitespace.rstrip()}!")

# prefixes can be removed from a string by inputting the expected prefix
# to the removeprefix() method.
example_url = 'https://example_url.null'
example_person = 'Mr. Doe'

# output "example_url.null"
print(example_url.removeprefix('https://'))
print(example_person.removeprefix('Mr. '))

# To avoid syntax error be sure to wrap strings containing apostraphes with
# quotation marks. Reflecting on this document shows the interchangeability
# of apostraphes and quotations as wrappers to strings.
final = "A test of john's skill."

# "A test of john's skill."
print(final)