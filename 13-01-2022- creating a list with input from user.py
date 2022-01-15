#program 6:
#[123, 124, 125,]  
#Create a list and identify the length of list  ?  odd or even


l1 = []
n = int(input("Number of elements you want :"))

for i in range(0, n):
    l2 = int(input("Enter the elements you want in the list, no "+str(i+1)+":"))
    l1.append(l2)
    print(l1)

if (len(l1)) % 2 ==0:
    print("even")
else:
    print("odd")
  





