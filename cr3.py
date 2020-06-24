import math
def circle(r):
    a=r**2*math.pi
    return a
r=float(input("Enter radius of circle"))
print("Area of circle",circle(r))
