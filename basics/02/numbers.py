# add
print(1+4)
# subtract
print(5-1)
# multiply
print(2*3)
# divide
# (note that python will return float division by default. Floor division can be used by importing using `//`)
print(10/2)
print(10//2)

# exponential values
print(10**2)

# python also supports the use of the order of operations, meaning several
# operations can be used in one expression.
print((2+3)*2)

# float addition
print(0.1+0.1)

# arbitrary values will be present as python attempts to represent the
# as precisely as possible
print(0.2+0.1)
# 0.30000000000000004

# mixing floats and integers will by default return a float value similarly to
# dividing
print(1+2.0)

# underscores can be used to make digit placement, they will be ignored by default
print(123_456_789)
print(12_3)

# values can be assigned to multiple variables in a single instance, helping
# shorten code.
x, y, z = 0, 1, 2

print(f"{x}\n{y}\n{z}")

# Python is a dynamically typed language
# This means that variables are dictated at runtime rather than at compile time like C++

# indicates the maximum user quantity
# caps can be used as an indication that a variable is constant
FAKE_MAX_USERS = 10