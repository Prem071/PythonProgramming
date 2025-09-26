# 1. write a program to store the odd numbers from 0 to 100.

a= 0
b=[]
while a<=100:
    if(a%2!=0):
        b.append(a)
        a=a+1
    else:   
        a=a+1

print(b)
       

    