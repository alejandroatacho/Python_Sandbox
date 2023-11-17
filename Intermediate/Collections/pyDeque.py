#8 collections deque

import collections
from collections import deque

# 1. Deque is a double-ended queue, it allows you to add and remove elements from both ends of the collection.

d = deque("hello")
print (d)
d.append(' looking good ')
d.append (2023)
print(d)
d.appendleft("we got here")
d.extend('5 2 3')
d.extendleft ('before you,')
print(d)
d.rotate (-2) #or do positive number to move them opposite direction
print(d)


f = deque("hello", maxlen=5) #max length
print(f)
f.append(1)
print (f)