# /usr/bin/python3
# simple Monte Carlo Analysis of Monty Hall Problem

from random import randint

s = 0

for i in range(0, 1000000):
    c = randint(0, 2) #car is placed
    p = randint(0, 2) #player chooses door

    #moderator opens door with goat
    if p == c:
        p = (c+1) % 3 #player was at car, moves to other door with goat
    else:
        p = c #player moves from goat to car

    if p == c:
        s += 1

s = s / 1000000
print(str(s))
