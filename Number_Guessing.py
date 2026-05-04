import random

num = random.randint(1, 10)

while True:
        player = input("Guess Number: ")

        if not player.isdigit():
                print("Please, Enter A Valid Number!")
                continue

        you = int(player)

        if (you < num):
                print("Your Guess Is Smaller!")
        elif (you > num):
                print("Your Guess Is Bigger!")
        else:
                print("Your Guess Is Correct!")
                break