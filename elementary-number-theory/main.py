s = r'''
a = 25
b = 8
q, r = divmod(25, 8)
print("%s = %s * %s + %s" % (a, b, q, r))'''.strip()
f = open('divmod.py', 'w'); f.write(s); f.close()
from latextool_basic import *
print(r'{\footnotesize %s}' % console(s))
print('The output is')
print(shell('python divmod.py'))

