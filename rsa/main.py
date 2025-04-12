from latextool_basic import *
p = Plot()
m = [[0,1],
     [0,0],
     [1,1],
]
table2(p, m, width=0.7, height=0.7,
rownames=[0,1,2],
colnames=['$a$', '$b$'],
rowlabel=None, collabel=None)
print(p)

