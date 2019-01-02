# Benjamin Readman
# Monty Hall Project Part 3
import random
lose = 0
win = 0
time = int(input("How many rounds of the game should be simulated: "))

if time > 10000 or time < 10:
    time = int(input("Please enter a number between 10 and 10,000: "))
else:
    sos = input("Should the player switch or stay? ")
    if sos != 'switch' and sos != 'stay':
        print('Must enter either "switch" or "stay"')
        sos = input("Please try again: ")
    elif sos == "switch":
        for x in range(time+1):
            car = random.randint(1, 3)
            player = random.randint(1, 3)
            if player == car:
                lose += 1
            elif player != car:
                win += 1
    elif sos == 'stay':
        for x in range(time+1):
            car = random.randint(1, 3)
            player = random.randint(1, 3)
            if player != car:
                lose += 1
            elif player == car:
                win += 1
    percent = win/time*100
    print("The player won ",win,'/',time,' games (',percent,'%)!',sep='')