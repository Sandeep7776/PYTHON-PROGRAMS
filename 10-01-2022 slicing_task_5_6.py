'''
Task5
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]

Output Prediction 

print(Li1[5][0]) #11
print(Li1[5][6]) #error
print(Li1[5][-2]) #55
print(Li1[5][7])   #error
print(Li1[6])      #error
print(Li1[5][5][1]) #222

print(Li1[-2][-1]) #error


print(Li1[-2][2:4]) #error
'''
#Task6:

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}


print(a[1][3][:2])               #py
print(a[2][10][1:])              #ello
print(a[2][40][3:5])             #en
print(a[40][1][:3])              #zoo
print(a[40][2][:3])              #Bot



print(a)
