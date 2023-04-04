#calculate area of triangle using heron's formula
#area = (s*(s-a)*(s-b)*(s-c))**0.5

a = float(input("first side of triangle: "))
b = float(input("second side of triangle: "))
c = float(input("third side of triangle: "))

s = (a+b+c)/2
print("s is:",s)

area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is",area)
