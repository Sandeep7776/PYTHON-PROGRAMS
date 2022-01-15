#program4:
#Get one string from user
#check whether string is palindrome or no

s = input()
pal = s[::-1] #This is the main logic to get a paliindrome
if s == pal:
    print ("* is a palindrome *", pal)
else:
    print("Not a palindrome")






