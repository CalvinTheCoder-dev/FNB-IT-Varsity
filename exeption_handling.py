
# This code demonstrates exception handling in Python.

x = -1

try:
    print(x)

except NameError:
    print("Variable 'x' is not defined.")

else:
    print("Everything went wrong")


if x < 0:
    raise Exception("x must be a non-negative integer")