#  1.

# l=[]
# for i in range(11):
#     if(i%2==0):
#         sq=i**2
#         l.append(sq)
# print(l)


 # 2.

# l=[]
# for i in range(1,51):
#         sq=i**2
#         l.append(sq)
# print(l)

# 3. 


cities=["Chenai", "Banglore", "Hyderabad", "Delhi", "Mumbai"]
cities=["chennai", "banglore", "hyderabad", "delhi", "mumbai"]


# upper=[]
# for i in cities:
#     upper.append(i.upper())
# print(upper)



# upper=[i.upper() for i in cities]
# print(upper)


# one={i:0 for i in range(20)}
# print(one)


print([x**2 for x in range(20) if x%2==0])