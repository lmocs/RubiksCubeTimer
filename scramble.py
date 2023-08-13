import random

moves = ('U','D','R','L','F','B',
         'U\'','D\'','R\'','L\'','F\'','B\'',
         'U2', 'D2', 'R2', 'L2', 'F2', 'B2')


def scramble():
    for i in range(25):
        print(random.choice(moves), end = " ")

scramble()