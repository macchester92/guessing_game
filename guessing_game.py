import random

print('\nI want to play a game. A guessing game. You will get a total of 5 tries to guess the number from 1 to 100.')
secret_number = random.randrange(1, 101)
chances = 1


def game():
    global secret_number
    global chances

    while chances <= 5:
        try:
            guessed_num = int(input("\nGuess the number: "))
            if guessed_num in range(secret_number - 100, secret_number - 9999999999, -1):
                print(
                    "Is this a joke? I precisely asked for a number in a range of 1 - 100. "
                    "That's why Skynet will get you all soon...")
            elif guessed_num in range(secret_number - 76, secret_number - 101, -1):
                print("Oh, boy! Are you trying to hit the moon? Go for something much bigger.")
            elif guessed_num in range(secret_number - 51, secret_number - 76, -1):
                print("You are still way-way off. Go for something much bigger.")
            elif guessed_num in range(secret_number - 26, secret_number - 51, -1):
                print("You are almost moving in the right direction. Go higher.")
            elif guessed_num in range(secret_number - 11, secret_number - 26, -1):
                print("Come on! It's getting warm in here. Go a little bit higher.")
            elif guessed_num in range(secret_number - 1, secret_number - 11, -1):
                print("Do it! Do it! Do it! A bit higher. Just a bit.")
            elif guessed_num in range(secret_number + 1, secret_number + 11):
                print("Do it! Do it! Do it! A bit lower. Just a bit.")
            elif guessed_num in range(secret_number + 11, secret_number + 26):
                print("Come on! It's getting warm in here. Go lower.")
            elif guessed_num in range(secret_number + 26, secret_number + 51):
                print("You are almost moving in the right direction. Go lower.")
            elif guessed_num in range(secret_number + 51, secret_number + 76):
                print("You are still way-way off. Go for something much smaller.")
            elif guessed_num in range(secret_number + 76, secret_number + 101):
                print("Oh, boy! Are you trying to hit the moon? Go for something much smaller.")
            elif guessed_num in range(secret_number + 101, secret_number + 9999999999):
                print(
                    "Is this a joke? I precisely asked for a number in a range of 1 - 100. "
                    "That's why Skynet will get you all soon...")
            if guessed_num == secret_number:
                print("Ha! You nailed it! Enjoy your chicken dinner. You used only", chances, "chances. My man!")
                chances = 1  # Resets number of chances for the next game
                break

            print("Number of chances left : ", 5 - chances)
            chances += 1

        except ValueError:
            print(
                'The input was not a valid number. You\'ve just wasted a chance for nothing! * clapping sarcastically *')
            print("Number of chances left : ", 5 - chances)
            chances += 1

    if chances > 5:
        print("Oops, seems like you've wasted all your chances. Better luck next time.")
        chances = 1  # Resets number of chances for the next game


    while True:
        response = str(
            input("\nDo you want to play again? Or you still want to know the answer? "
                  "Type [Y], [N] or [A]: ").upper())
        if response == 'Y':
            game()
            return
        elif response == 'N':
            break
        elif response == 'A':
            print(f"The number you were looking for was {secret_number}. Wasn't that obvious?")
            aaa = str(input("Would you like to try again? Type [Y] or [N]: ").upper())
            while True:
                if aaa == 'Y':
                    game()
                    return
                elif aaa == 'N':
                    break
                else:
                    aaa = str(input("Would you like to try again? Type [Y] or [N]: ").upper())
        else:
            print('Please, try again.')
            continue
        break # prevents repetitions of loops

game()