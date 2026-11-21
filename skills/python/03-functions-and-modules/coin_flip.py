from random import random

def flip_coin():
    if random() < 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())

def generate_even():
    return [i for i in range(1,50) if i % 2 == 0]

print(generate_even())