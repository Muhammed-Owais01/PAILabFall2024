from math import pi

def trapezoidArea(a, b, h):
    return 0.5*h*(a+b)
def paralleogramArea(a, b):
    return a*b
def cylinderArea(r, h):
    return 2*pi*r*h + 2*pi*r**2
def cylinderVolume(r, h):
    return pi*r**2*h

print(trapezoidArea(1, 3, 2))
print(paralleogramArea(2, 3))
print(cylinderArea(2, 2))
print(cylinderVolume(2, 2))