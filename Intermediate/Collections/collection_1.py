import collections
from collections import Counter

c = Counter('gallad'); #Count each letter how often they appear
print(c.most_common(2))
print(c)
c = Counter({'a':5, 'b':20});
print(c)
c = Counter(cats=4, dogs = 5);
d =['cats', 'dogs']
c.subtract(d)
print(c)
c.update(d)
print(c)