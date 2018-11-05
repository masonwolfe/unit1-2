name = str(input())
d = int(input())
w = int(input())
l = int(input())
from math import pi
cyl = pi * ((w/2)**2) * d
sqr = (w**2)*d
rect = w*l*d
print("Hi " + name + ", if you want to build a cylindrical pool it would be " + str(5.875*cyl) + " gallons.")

print("If you want to build a rectangular pool it would be " + str(7.5*rect) + " gallons.")
print("If you want to build a square pool it would be " + str(7.5*sqr) + " gallons.")