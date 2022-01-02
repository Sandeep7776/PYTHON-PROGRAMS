
#area of cone with formatting



radius=float(input("PLease enter te value of radius: "))
height=float(input("PLease enter te value of height: "))
pi=3.14

area_cone=(1/3  * pi * radius * height)

print("the area of the cone is :",int(area_cone))
print('the area of the cone with radius {}, height {}, and pi {} is :'.format(radius,height,pi),int(area_cone))

