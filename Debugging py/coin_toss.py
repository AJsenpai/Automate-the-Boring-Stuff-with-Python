import random

coin = {"tails": 0, "heads": 1}
guess = ""
while guess not in coin.keys():
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == coin[guess]:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    if toss == coin[guess]:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
