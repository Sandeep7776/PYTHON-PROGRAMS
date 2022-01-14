marks = int(input("Enter your marks: "))

if marks >= 50 and marks <=100 :
    print("congratulations!! you have passed.")

if marks >= 90 and marks <= 100:
    print("Your grade is 'A'.")

if marks >= 80 and marks <= 89:
    print("Your grade is 'B'.")

if marks >= 70 and marks <= 79:
    print("Your grade is 'C'.")

if marks >= 60 and marks <= 69:
    print("Your grade is 'D'.")

if marks >= 50 and marks <= 59:
    print("Your grade is 'E'.")


if marks <=49 and marks >= 0:
    print("FAILED")
    
if marks < 0 or marks > 100:
    print("INVALID ENTRY")
   
    
