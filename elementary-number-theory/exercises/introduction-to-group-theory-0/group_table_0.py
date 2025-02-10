import sys
sys.path.append('../../')
from group_table import *
p = Plot()
labels = ['$e$', '$a$', '$b$', '$c$']
data = [['', 'X', 'X', 'X'],
        ['', '', 'X', 'X'],
        ['', '', '', 'X'],
        ['', '', '', ''],
        
]
topleft = '$*$'
group_table(p, topleft=topleft, labels=labels, M=data)
print(p)
