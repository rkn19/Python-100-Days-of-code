import random

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    else:
        return 5

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    my_number = random.randint(1,100)
    print(f"The answer is {my_number}")
    life = difficulty()
    print(f"You have {life} attempts")
    while  life > 0:
        guess = int(input("Guess my number"))
        if guess > my_number:
            print("Too high")
            life -= 1
            print(f"You have {life} attempts left")
        elif guess < my_number:
            print("Too low")
            life -= 1
            print(f"You have {life} attempts left")
        else:
            print("Yaay!")
            break
    if life == 0:
        print("Game over you loser")
    else:
        print("You won!")
    exit()

game()

