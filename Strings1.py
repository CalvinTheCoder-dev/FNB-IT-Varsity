#Advanced Strings

message = "Good evening, Calvin"

print(message[0])     # Accessing the first character
print(message[-1])    # Accessing the last character
print(message[0:4])  # Slicing the first four characters
print(message[5:])   # Slicing from the fifth character to the end

print(len(message))  # Getting the length of the string
print(message.strip())  # Stripping whitespace from both ends
print(message.lower())  # Converting to lowercase
print(message.upper())  # Converting to uppercase

print(message.split(","))