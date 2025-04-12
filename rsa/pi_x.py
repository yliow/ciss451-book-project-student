import sys
import math

N = int(sys.argv[1]) # 100000

try:
    with_xlnx = bool(int(sys.argv[2]))
except:
    with_xlnx = True

width = '5in'
height = '3in'

prime = [1 for _ in range(N)]
pi = [0 for _ in range(N)]
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

for i in range(1, N):
    pi[i] = pi[i - 1] + prime[i]

points = [(0, 0)]
for i in range(1, N):
    if pi[i] == pi[i - 1]:
        points.append((i, pi[i]))
    else:
        points.append((i, pi[i - 1]))
        points.append((i, pi[i]))

if N < 10000:
    step = 1
elif N < 50000:
    step = 5
else:
    step = 10
data = ' '.join(['(%s,%s)' % (x,y) for (x,y) in points[::step]])

if with_xlnx:
    xlnx = r'\addplot[draw=red, domain=1:%s] {x/ln(x)};' % N
else:
    xlnx = ''
    
print(r"""
\begin{center}
\begin{tikzpicture}
\begin{axis}[width=%(width)s, height=%(height)s,
             xlabel={\mbox{}},
             xlabel style={name=xlabel}, 
             legend style={
                at={(xlabel.south)},
                yshift=-1ex,
                anchor=north,
                legend cell align=left,
                }
]
\addplot [black] coordinates {%(data)s};
%(xlnx)s
\legend{$\pi(x)$,
        $x/\ln x$}
\end{axis}
\end{tikzpicture}
\end{center}
""" % {'width':width, 'height':height, 'xlnx': xlnx, 'data':data})

primes = []
for i in range(N):
    if prime[i]: primes.append(i)
f = open('prime-table.txt', 'w')
s = ','.join(str(_) for _ in primes)
f.write(s)
f.close()
