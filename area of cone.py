#are of cone

pi=3.14
radius=654.25
height=90.65

area_cone=(1/3  * pi * radius * height)

print (type(area_cone))
print (area_cone)
print (int(area_cone))



#area of cone with formatting


pi=3.14
radius=654.25
height=90.65

area_cone=(1/3  * pi * radius * height)

print("the area of the cone is :",int(area_cone))
print('the area of the cone with radius {}, height {}, and pi {} is :'.format(pi,radius,height))
