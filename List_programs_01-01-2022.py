#creating a list

li = []
print(li)

#second method

li = list()
print(li)



#concatenating a list

li1 = [5,6]
li2 = [7,8]
l = li1+li2
print(l)

#addding elements to a list

ext = [8,9,1,5,6,7,8,1 ]
ext.extend(l)
print(ext)

#find the frequesncy of 8
print(ext.count(8))

#find the mean of the list

sum_list = sum(ext)
mean = sum_list/12
print(sum_list)
print(mean)

#sum, min, max

print(sum(ext))
print(min(ext))
print(max(ext))


#median of the list
print(ext[int((len(ext))/2)::50000])




#duplicate removal
new_list = set(ext)
print(new_list)
print(type(new_list))
