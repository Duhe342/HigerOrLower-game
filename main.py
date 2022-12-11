from random import randint, choice
import game_data
from copy import deepcopy
from art import logo, vs

data = game_data.data

def game():
    global data
    score = 0
    played = None
    winner = ''

    while True:
        if played is True and winner == "A":
           B = choice(data)
           data.remove(B)
        elif played is True and winner == "B":
            A = deepcopy(B)
            B = choice(data)
            data.remove(B)
        else:
           A = choice(data)
           data.remove(A)
           B = choice(data)
           data.remove(B)



        followA = A["follower_count"]
        followB = B["follower_count"]

        if followB > followA:
            winner = 'B'
        else:
            winner = 'A'

        print(logo)
        if played is not None:
            print(f"You are right! Current score: {score}")
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")

        print(vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

        answer = input("Who has more followers? Type 'A' or 'B': ")

        if answer == winner:
            score += 1
            played = True

        else:
            print("You are wrong")
            break
