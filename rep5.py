#4. 

letter_=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
even_index=[]
odd_index=[]
a=0
while a<26:
    if a%2==0:
        even_index.append(letter_[a])
    else:
        odd_index.append(letter_[a])
    a=a+1
print(even_index, odd_index)


