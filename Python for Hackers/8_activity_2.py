#write a program that promts the useer to enter their scor (out of 100) and
#display their corresponding grade based on the following crteria:
#
#Score 90 and above: Grade A
#Score 80 to 89: Grade B
#Score 70 to 79: Grade C
#Score 60 to 69: Grade D
#Score below 60: Grade F

score = int(input("Please enter your grade: "))

if score >= 90:
    print("Grade = A")
elif score >= 80:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Grade F")