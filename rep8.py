# 1. 

input="mississippi"

# output={'M':1, 'I':4, 'S':4, 'P':2}

inp=list(input)
out={}
for i in inp:
    if i in out:
        out[i]=out[i]+1
    else:
        out[i]=1   
print(out) 