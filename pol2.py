from math import tan,pi
sides=int(input("Enter the number of sides:"))
length=float(input("Enter length of sides:"))
area=sides*(length**2)/(4*tan(pi/sides))
print("Area of regular polygon is:",area)
