#data type conversions

#conversion of int to float: 1
a=20
b=30
c=a * b
print (float(c))

#conversion of int to bool: 2
a=20
b=30
c=a * b
print (bool(c))

#conversion of int to srting: 3
a=20
b=30
c= a * b
print (str(c))





#conversion of float to int: 4
a=20.56
b=30.124
c= a * b
print (int(c))

#conversion of float to bool: 5
a=2.00124
b=3.01453
c= a * b
print (bool(c))

#conversion of float to string: 6
a=2.00124
b=3.01453
c= a * b
print (str(c))



'''
#conversion of srting to int: 7(TypeError: can't multiply sequence by non-int of type 'str)
a= '20'
b='50'
c=a*b
print(int(c))

#conversion of srting to bool: 8(TypeError: can't multiply sequence by non-int of type 'str')
a= "20"
print(bool(a))

#conversion of string to float: 9(TypeError: can't multiply sequence by non-int of type 'str')
a='365'
print(float(a))
'''


#conversion of boolean to integor: 10
value= True
print(int(value))
# it is returning the binary value
