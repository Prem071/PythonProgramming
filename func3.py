# 1. write a function which takes any two numbers as the input and the operation as the input and return the result.

def op(a,b,o):
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b      
    elif o=='/':
        return a/b      
    else:
        return "invalid operation"
    
print(op(1,2,'-'))