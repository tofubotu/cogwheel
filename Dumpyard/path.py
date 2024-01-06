import os
import sys

print(__file__)
print(os.path.abspath(__file__))
a=os.path.abspath(__file__)
print(a)
b=os.path.dirname(a)
print(b)
c=os.path.dirname(b)
print(c)
d=os.path.dirname(c)
print(d)
e=os.path.dirname(d)
print(e)
f=os.path.dirname(e)
print(f)
g=os.path.dirname(f)
print(g)

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parent_dir)
sys.path.append(parent_dir)
