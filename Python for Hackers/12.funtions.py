choice = int(input("What number would you like to choose"))

def function(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print("FIZZBUZZ")
        elif num % 5 == 0:
            print("FIZZ")
        elif num % 3 == 0:
            print("BUZZ")

        else:
            print(num)

function(choice)
