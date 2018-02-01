####This will be my file to create Nim###

#Author: Cody Whitaker

import random
import time

def introduce_user():
    '''Introduces the user to the game and how to play'''
    pass

def amount_of_balls_for_turn(x):
    '''Asks for the amount of balls the user would like to play per turn with
        and makes sure it's the right amount'''
    ballsTurn = input("How many balls would you take for your turn?")
    while int(ballsTurn) > 4 or int(ballsTurn) < 1:
        answer = input("NOPE! Pick the right amount dude. 1 to 4 balls is how many you can take. Pick again.")
    x = x - int(ballsTurn)
    if x == 0:
        print("Get rekt mate! The user has won.")
        exit()
    return x

def turns(totalBalls):
    '''takes care of each turn and computers turn'''
    if totalBalls % 5 == 1:
        totalBalls = (totalBalls - 1)
        print("There are now " + str(totalBalls) + " balls left.")
    elif totalBalls % 5 == 2:
        totalBalls = (totalBalls - 2)
        print("There are now " + str(totalBalls) + " balls left.")
    elif totalBalls % 5 == 3:
        totalBalls = (totalBalls - 3)
        print("There are now " + str(totalBalls) + " balls left.")
    elif totalBalls % 5 == 4:
        totalBalls = (totalBalls - 4)
        print("There are now " + str(totalBalls) + " balls left.")
    elif totalBalls % 5 == 5:
        totalBalls = (totalBalls - random.randint(1,4))
        print("There are now " + str(totalBalls) + " balls left.")
    if totalBalls == 0:
        print("The computer has won.")
        exit()
    return totalBalls

def main():
    introduce_user()
    x = int(input("How many balls would you like to play with?"))
    while x < 15:
        x = int(input("Dude, pick something larger than 15. Geez."))
    while x > 0:
        x = amount_of_balls_for_turn(x) # comment
        x = turns(x)

main()

