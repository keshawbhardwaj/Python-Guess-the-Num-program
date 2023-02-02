# Python-Guess-the-Num-program
#CodeWithHArry Excercise 3 Guess the number
n = 18
#program for guessing number

print("Guess The Number between 1 - 50")
print("Only 5 chances are available")
Chance_available = int()
while (Chance_available <= 5):
    Number = int(input("Enter the Guess: "))
    if Number < n:
        print("Guess a higher number")
        print("Number of Guess left:",5 - Chance_available)
    elif Number > n:
        print("Guess a lower number")
    else:
        print("Absolutely Correct Guess")
        break
        if Chance_available == 5:
            break
            print("No more guesses are left")
    Chance_available = Chance_available + 1
