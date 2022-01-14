s1 = set()
s2 = set()
print(type(s1))


#updating a set

set1 = {7,8,9,1,2,3,4,5,0}
set1.update(s1)
print(set1)

set2 = {4,5,6,0}
set2.update(s2)
print(set2)


#superset
print(set2.issuperset(set1))


#common elements
print(set1.intersection(set2))


#removing
set1.remove(8)
print(set1)


#discarding
set1.discard(0)
set2.discard(0)
print(set2)
print(set1)

#union
print(set1.union(set2))





