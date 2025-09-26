# 1. check the number is even or odd 

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd" 

n = int(input("Enter a number: "))
print(even_or_odd(n))