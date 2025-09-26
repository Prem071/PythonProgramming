# 1. given 3 angles of a triangle, check whether the triangle is valid or not


def is_valid_triangle(a, b, c): 
    return a + b + c == 180

a = int(input("Enter angle 1: "))  
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))
if is_valid_triangle(a, b, c):
    print("The triangle is valid.") 
else:
    print("The triangle is not valid.")
