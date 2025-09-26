suv1={"e1","e2","e3"}
suv2={"e1","e4","e6"}

print(suv1.union(suv2))#union
print(suv1.difference(suv2))#diff
print(suv1.intersection(suv2))#common
print(suv1.isdisjoint(suv2))#check disjoint or not
print(suv1.issubset(suv2))#checks ifsub set or not
print(suv1.issuperset(suv2))#checks if super set or not
print(suv1.symmetric_difference(suv2))#not common

print(list(suv1))