                         
#task 3( 01-12-2021) FIZZ BUZZ

x = int(input("Pls enter a number: "))

if x % 3 == 0 and x % 5 ==0 :
	print("Fizzbuzz")
elif x % 3 == 0:
	print("Fizz")
elif x % 5 == 0:
	print("Buzz")

else:
	print("invalid numero")

print("The fizz buzz program is over")
