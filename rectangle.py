
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

import calc

area = calc.area(length, width)
perimeter = calc.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")