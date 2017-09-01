#SriMatreNamah!
"""
class Counter(builtins.dict)
 |  Dict subclass for counting hashable items.  Sometimes called a bag
 |  or multiset.  Elements are stored as dictionary keys and their counts
 |  are stored as dictionary values.
"""
'''
 |  elements(self)
 |      Iterator over elements repeating each as many times as its count.
'''
In [44]: import collections
    ...:
    ...: c=collections.Counter('ASASADASAS')
    ...: print(c.elements())
    ...: print(*list(c.elements()))
    ...:
<itertools.chain object at 0x000001FF7057FB70>
A A A A A S S S S D

'''
 |  copy(self)
 |      Return a shallow copy.
'''
c=collections.Counter('ASASADASAS')
d=c.copy()
print(c.elements())
print(*list(c.elements()))
print(d.elements())
print(*list(d.elements()))
'''
 |  most_common(self, n=None)
 |      List the n most common elements and their counts from the most
 |      common to the least.  If n is None, then list all element counts.
 |
 |      >>> Counter('abcdeabcdabcaba').most_common(3)
 |      [('a', 5), ('b', 4), ('c', 3)]
'''

'''
 |  subtract(*args, **kwds)
 |      Like dict.update() but subtracts counts instead of replacing them.
 |      Counts can be reduced below zero.  Both the inputs and outputs are
 |      allowed to contain zero and negative counts.
 |
 |      Source can be an iterable, a dictionary, or another Counter instance.
 |
'''
In [47]: c=collections.Counter('ASASADASAS')
    ...: print(c.most_common())
    ...: d=c.subtract('ASA')
    ...: print(c.most_common())
    ...:
[('A', 5), ('S', 4), ('D', 1)]
[('A', 3), ('S', 3), ('D', 1)]

In [48]:
	
'''
 |  update(*args, **kwds)
 |      Like dict.update() but add counts instead of replacing them.
 |
 |      Source can be an iterable, a dictionary, or another Counter instance.
'''
In [49]: c=collections.Counter('ASASADASAS')
    ...: print(c.most_common())
    ...: d=c.update('ASA')
    ...: print(c.most_common())
    ...:
[('A', 5), ('S', 4), ('D', 1)]
[('A', 7), ('S', 5), ('D', 1)]
