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

def generate_odd(num):
    return sum([i for i in range(1, num) if i % 2 != 0])

print(generate_odd(40))


def speak(animal="dog"):
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'meow'
    elif animal == 'dog':
        return 'woof'
    return '?'
print(speak('pig'))
