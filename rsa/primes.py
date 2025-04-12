import sys
import math

N = 30
prime = [1 for _ in range(N)]
prime[0] = 0
prime[1] = 0

p = 2
while p <= math.sqrt(N):
    i = 2
    while i * p < N:
        prime[i * p] = 0
        i += 1
    p += 1
    while p <= math.sqrt(N) and prime[p] == 0:
        p += 1
points = []
for i, b in enumerate(prime):
    if b:
        points.append(i)
            
from latextool_basic import *
from latexcircuit import *
p = Plot()
p += Line(points=[(0,0), (N/3 + 1, 0)])
for x in points:
    X = POINT(x=round(x/3, 2), y=0, r=0.06, label=r'{\scriptsize $' + str(x) + '$}', anchor='north')
    p += str(X)

X = POINT(x=0, y=0, r=0, label=r'{\scriptsize $' + str(0) + '$}', anchor='north')
p += str(X)

print(p)
