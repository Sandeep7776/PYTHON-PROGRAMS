                                     
s= input()
#vowels= "a","e","i","o","u"
middle = s[int(len(s)/2)]
#middle = (s[int((len(s))/2):int((len(s))/2+1)])
print(middle)
if middle in "aeiou":
    print("THE MIDDLE TERM IS AN VOWEL!!!!",middle)
    
else:
    print("THe middle term is consonant",middle)


