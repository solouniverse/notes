""" 
**********************************************
	Tuple: Immutable (Read only) ordered sequence of items of datatype 
	mixed.
**********************************************
class tuple(object)
 |  tuple() -> empty tuple
 |  tuple(iterable) -> tuple initialized from iterable's items
 |
 |  If the argument is a tuple, the return value is the same object.
 |
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
 |
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
"""
'''Notes:
	1. Represented by () 
	2. Any iterable can be turned into tuple using tuple()
	3. Tuples are immutable, only read only operations are allowed.
	4. For more details run: help(()) 
'''
#Empty Tuple
var=tuple()
print(var)
'''Output: 
()							# Empty tuple
'''

#Non empty tuple
var=(1,2,3,4,5)
print(var)
'''Output: 
(1,2,3,4,5)
'''

#Count occurances of given elements
var=(1,2,3,4,5,1,1,1)
print(var.count(1))

#returns index of first occurance of given element
var=(1,2,3,4,5,1,1,1)
print(var.index(5))

var=(1,2,3,4,5,2,3,1,1,1)
print(var.index(1,5,9)) # find element 1 between indices 5&9

#Convert an iterable into tuple
In [2]: tuple('SriRama')
Out[2]: ('S', 'r', 'i', 'R', 'a', 'm', 'a')
In [3]: tuple('S')
Out[3]: ('S',)

In [4]: tuple(1)  # An integer is not an iterable
TypeError: 'int' object is not iterable


""" 
**********************************************
	List: Mutable ordered sequence of items of datatype mixed.
**********************************************
class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
"""
'''Notes:
	1. For more details run: help([]) 
'''
#
#Creation of a list
#
#Empty Tuple
var=list() # or []
print(var)
'''Output: 
[]						# Empty list
'''

#Non empty tuple
var=[1,2,3,4,5]
print(var)
'''Output: 
[1,2,3,4,5]
'''

#
# append object at the end of list. Works only with single items
#
In [11]: var=[1,2,3,4,5,1,1,1]
    ...: var.append(100)
    ...: print(var)
    ...:
[1, 2, 3, 4, 5, 1, 1, 1, 100]
#Object can be an iterable "but appended as a single element"
In [12]: var=[1,2,3,4,5,1,1,1]
    ...: var.append([100,11])
    ...: print(var)
    ...:
[1, 2, 3, 4, 5, 1, 1, 1, [100, 11]]
#Note: last element is a list.

#
# clear  the list
#
In [13]: var=[1,2,3,4,5,1,1,1]
    ...: var.clear()
    ...: print(var)
    ...:
[]

#
# copy a given list into another one
#
In [14]: var=[1,2,3,4,5,1,1,1]
    ...: var2=var.copy()
    ...: print(var,var2,sep='\n')
    ...: print("id(var):{}\nid(var2):{}".format(id(var), id(var2)))
    ...:
[1, 2, 3, 4, 5, 1, 1, 1]
[1, 2, 3, 4, 5, 1, 1, 1]
id(var):2263810057096
id(var2):2263809862344
#Check the ids are different for both lists so its a cofirmed copy

#
#Count occurances of given elements
#
var=[1,2,3,4,5,1,1,1]
print(var.count(1))

#
#extend the list with given iterable, doesn't allow non iterables 
#
In [15]: var=[1,2,3,4,5,1,1,1]
    ...: var2=list("SriRama")
    ...: var.extend(var2)
    ...: print(var)
    ...:
[1, 2, 3, 4, 5, 1, 1, 1, 'S', 'r', 'i', 'R', 'a', 'm', 'a']
#Note: TypeError occures if non iterable is passed Ex: var.extend(1)

#
#return index of first occurance of given element
#
In [16]: var=[1,2,3,4,5,1,1,1]
    ...: print(var.index(5))
    ...:
4

In [17]: var=[1,2,3,4,5,2,3,1,1,1]
    ...: print(var.index(1,5,9))	# find element 1 between indices 5&9
    ...:
7 
#Note:  Raises "ValueError" if the value is not present.

#
# insert object before given index
#
In [18]: var=[1,2,3,4,5,2,3,1,1,1]
    ...: var.insert(0,1010)
    ...: print(var)
    ...:
[1010, 1, 2, 3, 4, 5, 2, 3, 1, 1, 1]

In [19]: var=[1,2,3,4,5,2,3,1,1,1]
    ...: var.insert(-1,list('SriRama'))
    ...: print(var)
    ...:
[1, 2, 3, 4, 5, 2, 3, 1, 1, ['S', 'r', 'i', 'R', 'a', 'm', 'a'], 1]
#Note inserts before the index but not at the index

#
# pop the item at index (default last)
#
In [20]: var=[1,2,3,4,5,2,3,1,1,100]
    ...: print(var.pop(5),"has been poppedout just now!")
    ...: print("now the list is: ",var)
    ...:
2 has been poppedout just now!
now the list is:  [1, 2, 3, 4, 5, 3, 1, 1, 100]

In [21]: var=[1,2,3,4,5,2,3,1,1,100]
    ...: print(var.pop(),"has been poppedout just now!")
    ...: print("now the list is: ",var)
    ...:
100 has been poppedout just now!
now the list is:  [1, 2, 3, 4, 5, 2, 3, 1, 1]
#Notes: 
#1. Pops out last item if no index is given
#2. Raises IndexError if list is empty or index is out of range.

#
# removes first occurance of value
#
In [22]: var=[1,2000,3,4,5,2000,3,1,1,100]
    ...: var.remove(2000)
    ...: print("Now the list is: ",var)
    ...:
Now the list is:  [1, 3, 4, 5, 2000, 3, 1, 1, 100]
#Note: Raises ValueError if the value is not present.

#
# reverse list **IN PLACE**
#
In [26]: var=[1,2000,None,3,4,5,2,3,1,1,100,None]
    ...: var.reverse()
    ...: print("Now the list is: ",var)
    ...:
Now the list is:  [None, 100, 1, 1, 3, 2, 5, 4, 3, None, 2000, 1]

#
# sort list **IN PLACE**
#
In [23]: var=[1,2000,3,4,5,2,3,1,1,100]
    ...: var.sort()
    ...: print("Now the list is: ",var)
    ...:
Now the list is:  [1, 1, 1, 2, 3, 3, 4, 5, 100, 2000]

In [28]: var=list('SriRama')
    ...: var.sort()
    ...: print(var)
    ...:
['R', 'S', 'a', 'a', 'i', 'm', 'r']

In [29]: var=['Hanuman', "Rama", "Sita", 'Lashman' ]
    ...: var.sort()
    ...: print(var)
    ...:
['Hanuman', 'Lashman', 'Rama', 'Sita']

In [30]: var=[[1,2,3],[1,2,4],[0,1,2,3],[-1,23,1,15]]
    ...: var.sort()
    ...: print(var)
    ...:
[[-1, 23, 1, 15], [0, 1, 2, 3], [1, 2, 3], [1, 2, 4]]

#Notes:
#1. Make sure no 'None' are present is list will cause TypeError otherwise
#2. Make sure all items are of same datatype(int, str, list) will cause TypeError otherwise
#3. Doesn't  work with list elements are dict as it uses "<" for sorting


#
#Convert an iterable into list
#
In [31]: list('SriRama')
Out[31]: ['S', 'r', 'i', 'R', 'a', 'm', 'a']

In [32]: list('S')
Out[32]: ['S']

In [33]: list(1)  # An integer is not an iterable
TypeError: 'int' object is not iterable
