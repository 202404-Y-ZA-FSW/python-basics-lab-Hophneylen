import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess the number between one to hundred(1-100): ")
    
    #to check if user entered an integer
    if guess.isdigit():
        guess = int(guess)
        attempts += 1
        
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"correct! It took you {attempts} attempts.")
            break
    else:
        print("Please enter a valid number, specifically an integer.")
