# 1. 
input=["dog","f","horn","fight"]

# output=["dog":3,"f":1,"horn":4,"fight":5]

out={}
for i in input:
    out[i]=len(i)
print(out)