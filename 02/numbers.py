# basic operations such as addition (+), subtraction (-), multiplication (*),
# and division (/) can be performed in python.

# output 5
print(1+4)

# output 4
print(5-1)

# output 6
print(2*3)

# output 5.0
# note division will always return a float rather than an int
print(10/2)

# to use exponent values the terminal uses two mulitplication symbols (**)

# output 100
print(10**2)

# python also supports the use of the order of operations, meaning several
# operations can be used in one expression.

# output 10
print((2+3)*2)

# floats are present as per most programming languages

# output 0.2
print(0.1+0.1)

# arbitrary values will be present as python attempts to represent the
# as precisely as possible

# output 0.30000000000000004
print(0.2+0.1)

# mixing floats and integers will by default return a float value similarly to
# dividing

# output 3.0
print(1+2.0)

# when writing long numbers, underscores can be used to make digit placement
# more legible. Python will ignore underscores in any arrangement.
large_number = 123_456_789
small_number = 12_3

# output 123456789
print(large_number)

# output 123
print(small_number)

# values can be assigned to multiple variables in a single instance, helping
# shorten code.
x, y, z = 0, 1, 2

# output
# 1
# 2
# 3
print(f"{x}\n{y}\n{z}")

# constant variables are not built into Python. It is common among programmers
# to use all capital leters to indicate a constant variable.

# indicates the maximum user quantity
MAX_USERS = 10