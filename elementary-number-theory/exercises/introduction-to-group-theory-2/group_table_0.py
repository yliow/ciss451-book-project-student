import sys
sys.path.append('../../')
from group_table import *

p = Plot()
e = r'$(1)$'
a = r'$(1 \ 2)$'
b = r'$(1 \ 3)$'
c = r'$(2 \ 3)$'
d = r'$(1 \ 2 \ 3)$'
f = r'$(1 \ 3 \ 2)$'
labels = [e, a, b, c, d, f]
data = [[e, a, b, c, d, f],
        [a, e, d, f, f, c],
        [b, f, e, d, c, a],
        [c, d, f, e, a, b],
        [d, c, a, b, f, e],
        [f, b, c, a, e, d],
]
topleft = r'$\circ$'
group_table(p, topleft=topleft, labels=labels, M=data, width=1.8)
print(p)

