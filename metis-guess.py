#!/bin/python
import random

secret_number = random.randint(0, 100)
print secret_number
guess = -1
N = 1

while secret_number != guess:
    if N > 10:
        break
    guess = int(raw_input('Guess a number between 0 and 100 -->'))
    N = N + 1
    if guess < secret_number:
        print "your guess is low"
    elif guess > secret_number:
        print "your guess is high"
    else:
        print "you guessed right!"
