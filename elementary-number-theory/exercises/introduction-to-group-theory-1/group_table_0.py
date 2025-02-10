import sys
sys.path.append('../../')
from group_table import *
p = Plot()
labels = ['$0$', '$1$', '$2$']
data = [['$0$', '$1$', '$2$'],
        ['$1$', '$2$', '$0$'],
        ['$2$', '$0$', '$1$'],
]
topleft = '$+$'
group_table(p, topleft=topleft, labels=labels, M=data)
print("(a) The group table for $\Z/3$ is")
print(p)

p = Plot()
labels = ['$0$', '$1$', '$2$', '$3$']
data = [['$0$', '$1$', '$2$', '$3$'],
        ['$1$', '$2$', '$3$', '$0$'],
        ['$2$', '$3$', '$1$', '$0$'],
        ['$3$', '$0$', '$1$', '$2$'],
]
topleft = '$+$'
group_table(p, topleft=topleft, labels=labels, M=data)
print("(b) The group table for $\Z/4$ is")
print(p)
