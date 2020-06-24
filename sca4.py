from math import sin
r=float(input("Enter radius of circle:"))
a=int(input("Enter the angle:"))
area=(r*r*(a-sin(a)))/2
print("Area of segment of circle is:",a)
