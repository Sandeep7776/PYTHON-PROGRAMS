di = {1:["english","maths","science"],2:[10,20,30],3:["bio-botany","bio-zoology","algebra"]}
print(di,type(di))

# 3 and 4
print(di[3][0][::2])
print(di[3][2][:-6:-1])

# keys to tuple
print(tuple(di[1]))
print(tuple(di[2]))
print(tuple(di[3]))

#average of all number sin key 2

d = sum(di[2])
print (int(d/3))

