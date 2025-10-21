import random

n = random.randint(1, 100)
a = -1
guesses = 1
while a != n:
    a = int(input("Guess the number:"))
    if a < n:
        print("Enter higher number")
        guesses += 1
    elif a > n:
        print("Enter small number")
        guesses += 1

print(f"you have guess the correct number {n} in {guesses} times")
