#tuple
import collections
from collections import namedtuple
#namedtuple is a function that allows you to create your own object types.

# Point = namedtuple ('Point', 'x y z')
# Point = namedtuple ('Point', ['x', 'y', 'z'])

Point = namedtuple ('Point', {'x':0, 'y':0, 'z':0})

newP = Point(3,4,5)

print (newP)
print (newP.x,newP.y,newP.z)
print (newP._asdict())
print(newP._fields)

newP = newP._replace(y=10)
print(newP)

p2 = Point._make(['a','b','c'])
print(p2)