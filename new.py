
input=[[10,20,30],50,[20,10],[20]]

out=[]
for i in input:
    if(type(i)==list):
        for j in i:
            out.append(j)
    else:
        out.append(i)
print(out) 


