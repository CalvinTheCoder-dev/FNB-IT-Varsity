## This function greets a person with their name

def greet(name):
  print(f"Hello, {name}!")

greet("Calvin")

# This function adds two numbers and returns the result

def add(a, b):
  return a + b

result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")

# This function calculates the factorial of a number using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage of greet function

def greet(name, greeting = "Hello"):	
    print(f"{greeting}, {name}!")

    greet("Bob", "Hi")


