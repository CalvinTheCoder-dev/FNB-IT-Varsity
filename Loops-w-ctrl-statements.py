#Loops with control statements
#for

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop when "cherry" is found 
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        continue  # Skip the cherry when "cherry" is found, and , move to the next iteration
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        pass  # Do nothing when "cherry" is found, just continue the loop
    print(fruit)

#While

count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        break  # Exit the loop when count reaches 3