# Jared Jackson
# 10/09/10
# This is going to be like the previous game
# where the user has to guess the correct number
# only this time they will get unlimited guesses
# In this exercise i want to type most of it here, on github
# I want to do this to challenge myself even though it was not recommended
from random import *

input("CLICK HERE AND PRESS ENTER TO ACTIVATE")
print("""Woah, it's you again...
I really didn't expect you to be back so soon...
Especially after how badly you lost last time!!!
Do you need a hospital? Cuz you just got burned!!!!!
I was told that's how you humans speak\n""")

name = input("""Anyhow, I'm bad with names, so you'll have to remind me what your name was.
>>>""").title()
print("Ahh, yes. I remember now.")
print("Heh.")
print(f"So, {name}, I want you to play another game.")
print("And by another game, I mean is the same game.")
print("Yes, the infamous \"Guessing The Numbers\" game, but this time you will be allowed an infinite amount of guesses.")
input("""Sounds fun, right?
>>>""")
print("Too bad, I don't give a rats donkey.\n")
print("Alright, here we go\n")

input("PRESS ENTER TO START THE GAME\n")

rn = randint(1, 20)
guess = int(input("""Okay, you know the deal;
guess a number between 1 and 20.
>>>"""))

while guess < rn or guess > rn:
    print("""Nope!
    \b\b\b\b\bYou've got to guess again.""")
    guess = int(input(">>>"))
    if guess == rn:
        print("I thought that would have taken you way longer.")
        print("You see, us computers can do computations way faster than you homo sapiens.")
        print("Anyhow it's getting late, so I'm going to head back into hybernation")
        print(f"It was nice tormenting you {name}, I sure do hope to see you here again in the future.")
    elif guess < rn:
        print("Too low!.")
    elif guess > rn:
        print("Too high!.")


# I started working on this and I made sure I finished
# I got slightly stuck on the loop, hehe, get it...
# But I did this to test my self and see if i could figure out how to properly
# or at least somewhat, get the loop working
# The loop said "guess < rn or guess > rn or guess == rn:"
# and that was messing me up
# Prior to that, i had the loop say "guess == rn:" and "guess < rn:"
# And when that didn't work, I made three loops
# For me it was a matter of "How do I incorporate these if statements into the loop"
# Then my brain grew bigger and I connected the dots
# I was about to save it for later, to show the Prof. but I wouldn't have been happy.
