
#program2
#Get one string from user
#Find the middle letter
#find ascii value for the middle letter
#check whether ascii value is odd or even

s = (input())
middle_char = (s[int((len(s))/2):int((len(s))/2+1)])
print(middle_char)
print(ord(middle_char))   
if ord(middle_char) % 2 ==0:
    print("The ASCII char is even")
else:
    print("THe ASCII char is odd")





