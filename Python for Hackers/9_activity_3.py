#write a program that promts the useer to enter their scor (out of 100) and
#display their corresponding grade based on the following crteria:
#
#Score 90 and above: Grade A
#Score 80 to 89: Grade B
#Score 70 to 79: Grade C
#Score 60 to 69: Grade D
#Score below 60: Grade F
#but this time ask for age from whoever getting grade A and B. and if the age is less than 10 you have to give A+ and B+ correspondetly.

score = int(input("Please enter your score: "))
if score >= 90:
    age = int(input("Please enter your age: "))
    if age < 10:
        print("Your grade is A+")
    else:
        print("Your grade is A")
elif score >= 70:
    age = int(input("Please enter your age: "))
    if age < 10:
        print("Your grade is B+")
    else:
        print("Your grade is B")
elif score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")