# -*- coding: utf-8 -*-

from countries_capitals import countries_capitals
import random
import os

def clear():
    os.system("clear")
    if os.name == "nt":
        os.system("cls")



right = {}
wrong = {}
clear()
print "Welcome to <--Guess The Capital->>"
def game(our_dict):

    while True:

        country = random.choice(our_dict.keys())
        capital = our_dict[country]
        cap = capital.lower()

        guess = raw_input("Try to guess the capital of %s: "%country).lower()



        if guess == cap:
            print "You guessed right!"
            right[country] = capital
            del our_dict[country]
            while True:
                answer = raw_input("""\nDo you want to try & guess another one?
Type 'y' for yes or 'n' for no: """).upper()

                if answer == "Y":
                    clear()
                    break

                elif answer == "N":
                    clear()
                    print """Thank you for playing <--Guess The Capital->>!\n"""
                    return

                else:
                    clear()
                    print "You chose an invalid option!\nTry again!"
                    continue

        else:
            print "You guessed wrong!"
            wrong[country] = capital
            del our_dict[country]
            while True:
                answer = raw_input("""\nDo you want to try & guess another one?
Type 'y' for yes or 'n' for no: """).upper()

                if answer == "Y":
                    clear()
                    break

                elif answer == "N":
                    clear()
                    print """Thank you for playing <--Guess The Capital->>!\n"""
                    return

                else:
                    clear()
                    print "You chose an invalid option!\nTry again!"
                    continue

game(countries_capitals)

len_right = float(len(right))
len_wrong = float(len(wrong))
len_rw = len_right + len_wrong

print """You guessed %.0f right and %.0f wrong.\n
Your success rate is %.02f%%\n""" %(len_right, len_wrong, (len_right/len_rw)*100)

print "Your right answers: "
for item in right:
    print "%s: %s"%(item, right[item])
print "\n"

print "Your wrong answers: "
for item in wrong:
    print "%s: %s"%(item, wrong[item])
print "\n"
