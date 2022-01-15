#program5:
#two strings from user
#check if the vowels in both are equal count or not equal

str1 = input()
str2 = input()

vowel1 = 0
vowel2 = 0

for i in str1 :
    if i in "aeiou":
        vowel1 = vowel1 + 1
for i in str2 :
    if i in "aeiou":
        vowel2 = vowel2 + 1

print (vowel1)
print (vowel2)

if vowel1 == vowel2:
    print("equal")
else:
    print ("not equal")


# In[6]:


#alternate solution


str1 = input()
str2 = input()

vowel1 = 0
vowel2 = 0

vowel1 = str1.count("a")+ str1.count("e")+str1.count("i")+str1.count("o")+str1.count("u")
vowel2 = str2.count("a")+ str2.count("e")+str2.count("i")+str2.count("o")+str2.count("u")


print (vowel1)
print (vowel2)

if vowel1 == vowel2:
    print("equal")
else:
    print ("not equal")


# In[ ]:





# In[ ]:




