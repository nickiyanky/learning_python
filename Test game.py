  #Whats your name ?

import time
name = input('What is your name? ')
if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name must be maximum of 50 characters")

print('Hi ' + name)
time.sleep(.50)


         #favourite Color

favourite_color = input('What is your favourite color? ')
time.sleep(.50)
print('Seems like we both have same Taste, ' + 'I also like ' + favourite_color )
time.sleep(2.1)

         #Person Age
person_age = input('What is your Age? ')
time.sleep(.50)
print("What a coincidence i am " + person_age + ' too')

import random
import time

#!/usr/bin/env python3

import random
guess = 0
number = random.randint(1, 10)
tries = 1

        #Guess Game

print("Hey " + name + " wanna play a game" )

question = input("Would you like top play A Game? [Y/N] ")
if question == "n":
    print("oh..okay")

if question == "y" or question == "" or question == "" or question == "":
    print("I am thinking of a number between 1 and 10")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess lower...")
    if guess < number:
        print("Guess higher..")
    while guess != number:
        tries += 1
        guess =int(input("Try Again: "))
        if guess < number:
            print("Guess Higher")
        if guess == number:
            print("You are right! you win! The number was", number, \
                  "and took you ", tries, " tries")



         #Facts

facts = input("Hey Wanna Know some Fun Facts about our World [Y/N] ")
if facts == "n" or facts == "N":
    print('No Problem ')

if facts == "y" or "Y":
    print("1. North Korea and Cuba are the only places you can't buy Coca-Cola.")
    time.sleep(4)
    print("2. the longest place name on the planet is 85 letters long")
    time.sleep(4)
    print("3. If you make ice cubes with tap water, they will be white; if you use boiled water, they will be transparent")
    time.sleep(4)
    print("4. You spend so little electricity charging your smartphone that even if you calculated the yearly cost of it, it would be less than $1.")
    time.sleep(4)
    print("5. In order to burn just 1 calorie, you need to click a mouse button 10 million times.")
    time.sleep(4)
    print("6. When you take a hot bath, you burn as many calories as you would if you went for a 30-minute walk.")
    time.sleep(4)
    print("7. Bananas have a curved shape because they reach for the sunlight when they grow.")
    time.sleep(4)
    print("8. The Mona Lisa was in Napoleon Bonaparte's bedroom for a few years.")
    time.sleep(4)
    print("9. The Pokemon characters Hitmonlee and Hitmonchan were named after Bruce Lee and Jackie Chan.")
    time.sleep(4)
    print("10. 99% of the microbes that live inside humans are unknown to science.")