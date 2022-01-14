t1 = (1,4,5,6,7,8)
t2 = (5,6,7,8,9)
print(t1,type(t1))
print(t2,type(t2))


#common elements between the tuples==002
commom_elements = tuple(set(t1) and set(t2))
print (commom_elements)


#concatenate and remove dublicates==003
elements = tuple(set(t1+t2))
print(elements)


#index===004
print(elements.index(9))


#multiply===005
for element in elements:
	print(element*3,"\t\n")
