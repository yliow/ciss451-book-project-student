def inv(x):
    for y in range(1, 26):
        if (x * y) % 26 == 1:
            return y
    return None
from latextool_basic import *
p = Plot()
m00 = [[r'$\text{ \scriptsize{ \( x \pmod{26} \) }}$']]
m10 = [[r'{\scriptsize %s}' % i] for i in range(26)]
m01 = [[r'$\text{ \scriptsize{ \( x^{-1} \pmod{26} \) } }$']]
m11 = [[r'{\scriptsize None}']] + [[r'{\scriptsize %s}' % str(inv(i))] for i in range(1, 26)]
M = [[m00, m01],
     [m10, m11]]
N = table3(p, M, width=2.5, height=0.5)
print(p)

