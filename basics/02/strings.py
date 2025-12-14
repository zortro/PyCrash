# create variable and print variable to terminal
message = "Hello Python, this message is contained in a variable!"
print(message)

# method: title() will convert the first letter in all strings to uppercase
name = "john doe"
print(name.title())

# method: upper() will convert all to uppercase
print(name.upper())

# method: lower() will convert all to lowercase
print(name.lower())

first = "johnny"
last = "doe"

# f strings are used to stringify variables
full = f"{first} {last}"

print(full)

print(f"Hello, {first.title()} {last.title()}. Welcome to Python!")

# f sttrings can be pre stored in a variable
second_message = f"Greetings {first.title()} {last.title()}. I am... {name.upper()}!!"

print(second_message)

# \t will tab over the next printed text that follows
print("\tPython!")

# \n will create a new line for the next text that follows
print("Languages:\nPython\nJavaScript")

whitespace = 'Python '

# method rstrip() will strip any white space from a value
print(f"example with whitespace {whitespace}!")

print(f"example without whitespace {whitespace.rstrip()}!")

# method removeprefix() will remove any matching variable that is passed through
example_url = 'https://example_url.null'
example_person = 'Mr. Doe'

print(example_url.removeprefix('https://'))
print(example_person.removeprefix('Mr. '))

# avoiding common syntax error:
final = "A test of john's skill."

print(final)