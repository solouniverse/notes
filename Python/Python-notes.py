#SrimatreNamaha!
"""
Table of contents:
1. print()
2. input()
3. Data Types:
	a. Tuples
	b. Lists
	c. Dictionaries
	d. Sets
	e. Strings
	
"""

""" 
**********************************************
	print() print to screen
**********************************************
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.	
"""

print("Sri MatreNamaha!")	# Simple String
'''Output:
Sri MatreNamaha!
'''
x=1
y='Sri'
z=[1,2,3,4]
a={0:123,1:'qwe'}
print(x,y,z,a)				# A list of variables
'''Output:
1 Sri [1, 2, 3, 4] {0: 123, 1: 'qwe'}  # seprated by spaces
'''
print(x,y,z,a, sep='-')
'''Output:
1-Sri-[1, 2, 3, 4]-{0: 123, 1: 'qwe'}
'''
print(x,y)					#print them in separate lines
print(z,a)					#
'''Output:
1 Sri
[1, 2, 3, 4] {0: 123, 1: 'qwe'}
'''

print(x,y,end=" ")			#print " " instead of '\n' at the end of line
print(z,a)					#keeps both print outputs in a single line
'''Output:
1 Sri [1, 2, 3, 4] {0: 123, 1: 'qwe'}  
'''


# Formatted print()
#Using "str.format()"
In [14]: var=[1,2,3,4,5,1,1,1]
    ...: var2=var.copy()
    ...: print(var,var2,sep='\n')
    ...: print("id(var):{}\nid(var2):{}".format(id(var), id(var2)))
    ...:
[1, 2, 3, 4, 5, 1, 1, 1]
[1, 2, 3, 4, 5, 1, 1, 1]
id(var):2263810057096
id(var2):2263809862344


""" 
**********************************************
	input() Read input from keyboard, strip trailing '\n'
**********************************************
input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
"""

value=input("Enter: ")		# prompts with given string "Enter"
print(value)				
'''Output:
Enter: Srirama
Srirama
'''

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

""" 
**********************************************
	dict - dictionaries
**********************************************
class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |
 |-> Methods
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
"""
#
#Creation of a dictionary
#
#Empty dictionary
In [34]: var=dict()
    ...: print(var)
    ...:
{}

In [35]: var={}
    ...: print(var)
    ...:
{}

#Non empty tuple
# From Key value pairs
In [36]: var={1:123,2:345,1:234,2:678}
    ...: print(var)
    ...:
{1: 234, 2: 678}
In [37]: d = dict([(1,'a'),(2,'b'),(3,'c'),('d',4)])
    ...: print(d)
    ...:
{1: 'a', 2: 'b', 3: 'c', 'd': 4}
#Notes: 
#1. A key can have only 1 value.
#2. If more than 1 values are assigned to the same key last value will be asigned

#
# clear the dictionary
#
In [38]: var={1:123,2:345,1:234,2:678}
    ...: var.clear()
    ...: print(var)
    ...:
{}

#
# copy shallow copy
#

In [39]: var={1:123,2:345,1:234,2:678}
    ...: var2=var
    ...: shallow_var2=var.copy()
    ...: print("var=\t{}\nvar2=\t{}\nshallow_var2={}".format(var,var2,shallow_var2))
    ...: print("id(var)=\t%d\nid(var2)=\t%d\nid(shallow_var2)=%d" %(id(var),id(var2),id(shallow_var2)))
    ...:
    ...:
var=    {1: 234, 2: 678}
var2=   {1: 234, 2: 678}
shallow_var2={1: 234, 2: 678}
id(var)=        2263820659952
id(var2)=       2263820659952
id(shallow_var2)=2263820467512
#Notes: 
#1. Simple sopy using '=' will simple copy its reference. 
#2. To make physical copy of any object use .copy() method.

#
# fromkeys using an iterable
#
In [40]: var=list("srirama")
    ...: print(dict.fromkeys(var))
    ...:
{'s': None, 'r': None, 'i': None, 'a': None, 'm': None}
#Set default value by passing value
In [41]: var=list("srirama")
    ...: value=1001
    ...: print(dict.fromkeys(var,value))
    ...:
{'s': 1001, 'r': 1001, 'i': 1001, 'a': 1001, 'm': 1001}

#
# dict.get() get the value of given key
#

# Access values using dict[key]
In [42]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print(var[2])
    ...:
Rama

In [43]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print(var.get(2))
    ...: print(var.get(5)) # return None but dont raise KeyError if key doesnt exists
    ...: print(var.get(5,"Hanuman")) #return given value if key doesnt exists
    ...:
Rama
None
Hanuman
#Notes:
#1. Using dict[key] will cause a KeyError if key isnt valid.
#2. Using dict.get will return 'None' or default value passed if key isnt valid.

#
# dict.items() 
#
In [44]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print(type(var.items()))
    ...: print(var.items())
    ...: print(list(var.items()))
    ...:
<class 'dict_items'>
dict_items([(1, 'Sri'), (2, 'Rama'), (3, 'Chandra'), (4, 'Sita')])
[(1, 'Sri'), (2, 'Rama'), (3, 'Chandra'), (4, 'Sita')]

#
# dict.keys()
#
In [45]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print(type(var.keys()))
    ...: print(var.keys())
    ...: print(list(var.keys()))
    ...:
<class 'dict_keys'>
dict_keys([1, 2, 3, 4])
[1, 2, 3, 4]

#
# dict.pop(key,[default value]) "key" is mandatory, "default value" is optional
#
In [46]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print(var.pop(3)) #key is mandatory param here
    ...: print(var)
    ...:
Chandra
{1: 'Sri', 2: 'Rama', 4: 'Sita'}

var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
print(var.pop(5,"Hanuman")) #Return default value if key isnt found and dont raise KeyError
print(var)
#Notes:
#1. Unlike list.pop() key is mandatory here.
#2. If given key isnt found raises 'KeyError' if default value isnt passed

#
# dict.popitem() #doesn't take any params, returns (key, value)
#

In [48]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print(var.popitem())
    ...: print(var.popitem())
    ...: print(var)
    ...:
(4, 'Sita')
(3, 'Chandra')
{1: 'Sri', 2: 'Rama'}
#Note: Raises 'KeyError' if dict is empty

#
# dict.setdefault(key[,default value])
#
In [49]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print( "Value : %s" %  var.setdefault(3, None)) #returns value if exists
    ...: print( "Value : %s" %  var.setdefault('Age', 123))#returns new value if doesn't exists
    ...: print(var)
    ...:
Value : Chandra
Value : 123
{1: 'Sri', 2: 'Rama', 3: 'Chandra', 4: 'Sita', 'Age': 123}

In [51]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print( "Value : %s" %  var.setdefault(3)) #returns value if exists
    ...: print( "Value : %s" %  var.setdefault('Age'))#returns 'None' 
    ...: #if doesn't exist & dont raise KeyError just like dict.get()
    ...: print(var)
    ...:
Value : Chandra
Value : None
{1: 'Sri', 2: 'Rama', 3: 'Chandra', 4: 'Sita', 'Age': None}
#Notes:
#1. Works just like dict.get() but creates new key,value pair if doesnt exists

#
# dict.update()
#
#update with another dict
In [52]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: var2={3:"Sri",5:"lakshman",6:"Hanuman"}
    ...: var.update(var2)
    ...: print(var)
    ...:
{1: 'Sri', 2: 'Rama', 3: 'Sri', 4: 'Sita', 5: 'lakshman', 6: 'Hanuman'}
#update with a list of key,value pairs
In [53]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: var2=[(3,"Sri"),(5,"lakshman"),(6,"Hanuman")]
    ...: var.update(var2)
    ...: print(var)
    ...:
{1: 'Sri', 2: 'Rama', 3: 'Sri', 4: 'Sita', 5: 'lakshman', 6: 'Hanuman'}
#Note: Values of new dictionary will overwrite existing dictionary for matched keys.

#
# dict.values() 
#
In [54]: var={1:"Sri",2:"Rama",3:"Chandra",4:"Sita"}
    ...: print(type(var.values()))
    ...: print(var.values())
    ...: print(list(var.values()))
    ...:
<class 'dict_values'>
dict_values(['Sri', 'Rama', 'Chandra', 'Sita'])
['Sri', 'Rama', 'Chandra', 'Sita']



""" 
**********************************************
	Sets
**********************************************
class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |
 |  Build an unordered collection of unique elements.
 |
 |  add(...)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(...)
 |      Remove all elements from this set.
 |
 |  copy(...)
 |      Return a shallow copy of a set.
 |
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |
 |      (i.e. all elements that are in this set but not the others.)
 |
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |
 |      If the element is not a member, do nothing.
 |
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |
 |      (i.e. all elements that are in both sets.)
 |
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(...)
 |      Report whether another set contains this set.
 |
 |  issuperset(...)
 |      Report whether this set contains another set.
 |
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |
 |      (i.e. all elements that are in exactly one of the sets.)
 |
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |
 |  union(...)
 |      Return the union of sets as a new set.
 |
 |      (i.e. all elements that are in either set.)
 |
 |  update(...)
 |      Update a set with the union of itself and others.
"""
#
# Creation of a set
#
In [55]: var={100,5,5,4,1,2,3,4,5} 
    ...: print(var)
    ...:
{1, 2, 3, 4, 100, 5} 

In [56]: var=list("SriRama")
    ...: var=set(var)
    ...: print(var)
    ...:
{'i', 'r', 'R', 'a', 'm', 'S'}
#Note: Removes duplicates form a unique elements collection

#
# set.add() add new item to set ignore is already exists
#
In [57]: var={100,5,5,4,1,2,3,4,5}
    ...: print(var)
    ...: var.add(1001)
    ...: print(var)
    ...: var.add(100)
    ...: print(var)
    ...:
{1, 2, 3, 4, 100, 5}
{1, 2, 3, 4, 100, 5, 1001}
{1, 2, 3, 4, 100, 5, 1001}
#Note: Ignores existing item addition as set is an unique item collection

#
# set.clear() empty a set
#
In [58]: var={100,5,5,4,1,2,3,4,5}
    ...: var.clear()
    ...: print(var)
    ...:
set()

#
# set.copy() Creat a shallow copy 
#

In [59]: var={100,5,5,4,1,2,3,4,5}
    ...: var2=var
    ...: shallow_var2=var.copy()
    ...: print(var,var2,shallow_var2, sep='\n')
    ...: print(id(var),id(var2),id(shallow_var2), sep='\n')
    ...:
{1, 2, 3, 4, 100, 5}
{1, 2, 3, 4, 100, 5}
{1, 2, 3, 4, 100, 5}
2263810187048
2263810187048
2263810186152

#
# set.difference(set2) returns difference between sets
#

In [60]: var={100,1,2,3,4,5}
    ...: var2={100,5,-1,22,33,44,55}
    ...: print(var,var2, sep='\n')
    ...: print(var.difference(var2))
    ...:
{1, 2, 3, 100, 4, 5}
{33, 100, 5, 44, 22, 55, -1}
{1, 2, 3, 4}

In [61]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var2={100,5,-1,22,33,44,55}
    ...: var3=set("Srirama")
    ...:
    ...: print(var,var2,var3, sep='\n')
    ...: print("Differenceis:",var.difference(var2,var3))
    ...:
{1, 2, 3, 100, 4, 5, 'r', 'i', 't', 'a', 'S'}
{33, 100, 5, 44, 22, 55, -1}
{'i', 'r', 'a', 'm', 'S'}
Differenceis: {1, 2, 3, 4, 't'}

#Note: Returns elements from reference set that are not found in given sets.
# or lists difference elements only from first set (first_set.differance(set1,set2...setn))

#
# set.difference_update(set1,set2...setn) Remove all elements of given sets from this set
#

In [62]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var2={100,5,-1,22,33,44,55}
    ...: var3=set("Srirama")
    ...:
    ...: print(var,var2,var3, sep='\n')
    ...: var.difference_update(var2,var3)
    ...: print("Now the set is:",var)
    ...:
{1, 2, 3, 100, 4, 5, 'r', 'i', 't', 'a', 'S'}
{33, 100, 5, 44, 22, 55, -1}
{'i', 'r', 'a', 'm', 'S'}
Now the set  is: {1, 2, 3, 4, 't'}

#
# set.discard(single element) # Removes "element" from a set
#
In [64]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var.discard(100)
    ...: var.discard(1001)		
    ...: print("Now the set is : ",var)
    ...:
Now the set is :  {1, 2, 3, 4, 5, 'r', 'i', 't', 'a', 'S'}
#Notes: 
#1. Takes only 1 element as argument
#2. If the element is not a member, do nothing.

#
# set.intersection(set1,set2,set3...setn) # return intersection of given sets
#

In [68]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var2={100,5,-1,22,33,44,55,"S",'a'}
    ...: print(var.intersection(var2))
    ...: var3=set("Srirama")
    ...: print(var.intersection(var2,var3))
    ...: print(set.intersection(var2,var3,var)) # Even this is allowed!!
    ...:
{'a', 100, 5, 'S'}
{'a', 'S'}
{'a', 'S'}
#Note:'set.intersection(var2,var3,var)' is same as 'var.intersection(var2,var3)' 

#
# set1.intersection_update(set2,set3,set4...setn) # update set1 with 
# intersection of given givensets
#

In [69]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var2={100,5,-1,22,33,44,55,"S",'a'}
    ...: var.intersection_update(var2)
    ...: print(var)
    ...: var3=set("Srirama")
    ...: var.intersection_update(var2,var3)
    ...: print(var)
    ...:
{'a', 100, 5, 'S'}
{'a', 'S'}

#
# set.isdisjoint(set1,set2,set3,...setn)
#
In [70]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var2={100,5,-1,22,33,44,55,"S",'a'}
    ...: print(var.isdisjoint(var2))
    ...: print(var.isdisjoint({-1,-2,-3}))
    ...: print(set.isdisjoint(var,var2))
    ...: print(set.isdisjoint(var,{-1,-2,-3}))
    ...:
False
True
False
True
#Note: set.isdisjoint(var,var2) is same as var.isdisjoint(var2)

#
# set1.issubset(set2) True if set1 is a subset of set2
#
In [71]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: print(var.issubset({100}))
    ...: print({100}.issubset(var))
    ...: print({100,99,98,97,1}.issubset({98,97}))
    ...: print({97,1}.issubset({100,99,98,97,1}))
    ...:
False
True
False
True
#Note: Takes only one set as argument or TypeError

#
# set1.issubset(set2) True if set1 is a superset of set2
#

In [72]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: print(var.issuperset({100}))
    ...: print({100}.issuperset(var))
    ...: print({100,99,98,97,1}.issuperset({98,97}))
    ...:
True
False
True
#Note: Takes only one set as argument or TypeError

#
# set.pop() Remove and return an arbitrary set element
#
In [73]: var={98,97,1}
    ...: print(var.pop())
    ...: print(var)
    ...: print(var.pop())
    ...: print(var)
    ...: print(var.pop())
    ...:
97
{98, 1}
98
{1}
1
#Notes:
#1. pops arbitrary set elements
#2. Raises KeyError if set is empty
#3. Takes no arguments

#
# set.remove(single element) 
#

In [74]: var={98,97,1}
    ...: var.remove(98)
    ...: print(var)
    ...: print(var.remove(97))
    ...: print(var)
    ...:
{97, 1}
None
{1}
#Notes:
#1. Takes only 1 element but not set!
#2. raises KeyError if element is not found or set is empty

#
# set.symmetric_difference(set1,set2,...setN)
#   Return the symmetric difference of two sets as a new set.
#
In [77]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var2={100,5,-1,22,33,44,55,"S",'a'}
    ...: print(var.symmetric_difference(var2))
    ...: print(set.symmetric_difference(var,var2))
    ...:
    ...:
{1, 2, 3, 4, 22, 33, 'i', 'r', 44, 't', 55, -1}
{1, 2, 3, 4, 22, 33, 'i', 'r', 44, 't', 55, -1}

#Note: Returns uniques items from both sets as a set

#
# set1.symmetric_difference_update(set2,set3,...setN)
#   Updates set1 with the symmetric difference of two sets.
#
In [78]: var={100,1,2,3,4,5,'S','r','i','S','i','t','a'}
    ...: var2={100,5,-1,22,33,44,55,"S",'a'}
    ...: var.symmetric_difference_update(var2)
    ...: print(var)
    ...:
    ...:
{1, 2, 3, 4, 'r', 'i', 33, 44, 't', 22, 55, -1}
#Notes: set1 is updated with unique elements from all sets.

#
# set.union(...) Return the union of sets as a new set.
#
In [79]: var={100,1,2,}
    ...: var2={100,1,-1,33,44,}
    ...: print(var.union(var2))
    ...: print(set.union(var,var2))
    ...:
{1, 2, 33, 100, 44, -1}
{1, 2, 33, 100, 44, -1}
#Note: returns a set with elements from both sets

#
# set1.update(set2) 
#	Update a set with the union of itself and others.
#
In [80]: var={100,1,2,}
    ...: var2={100,1,-1,33,44,}
    ...: var.update(var2)
    ...: print(var)
    ...:
{1, 2, 33, 100, 44, -1}
#Note: Extend set1 with elements of set2


""" 
**********************************************
	String Objects
**********************************************
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.	
 |
 |  capitalize(...)
 |      S.capitalize() -> str
 |
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |
 |  casefold(...)
 |      S.casefold() -> str
 |
 |      Return a version of S suitable for caseless comparisons.
 |
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |
 |  encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |
 |  expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
|
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |
 |      Like S.find() but raise ValueError when the substring is not found.
 |
 |  isalnum(...)
 |      S.isalnum() -> bool
 |
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |
 |  isalpha(...)
 |      S.isalpha() -> bool
 |
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |
 |  isdecimal(...)
 |      S.isdecimal() -> bool
 |
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
 |
 |  isdigit(...)
 |      S.isdigit() -> bool
 |
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |
 |  isidentifier(...)
 |      S.isidentifier() -> bool
 |
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".
 |
 |  islower(...)
 |      S.islower() -> bool
 |
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |
 |  isnumeric(...)
 |      S.isnumeric() -> bool
 |
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |
 |  isprintable(...)
 |      S.isprintable() -> bool
 |
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.
 |
 |  isspace(...)
 |      S.isspace() -> bool
 |
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |
 |  istitle(...)
 |      S.istitle() -> bool
 |
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
 |
 |  isupper(...)
 |      S.isupper() -> bool
 |
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |
 |  join(...)
 |      S.join(iterable) -> str
 |
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).  
|
 |  lower(...)
 |      S.lower() -> str
 |
 |      Return a copy of the string S converted to lowercase.
 |
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
 |
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 | 
|
 |  lower(...)
 |      S.lower() -> str
 |
 |      Return a copy of the string S converted to lowercase.
 |
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |
 |      Return -1 on failure.
 |
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |
"""
#
# Creating of string object
#
In [1]: strng="Sri Matrenamaha"

In [2]: print(strng)
Sri Matrenamaha

In [3]: strng="12331213"

In [4]: strng
Out[4]: '12331213'

In [5]: number=12311123

In [6]: strng=str(number)

In [7]: strng
Out[7]: '12311123'

#
# str.capitalize() #Return a capitalized version of S, i.e. make the first
#				    character have upper case and the rest lower case
#
strng="sri Matrenamaha"
print(strng.capitalize())
print(strng)

#
In [10]: strng="sRi RAMA"
    ...: print(strng.capitalize())	# Return capilized version
    ...: print(strng)				# Doesn't change the original string variable
    ...:
Sri rama #Only first letter is upper cased all other letters are lower cased
sRi RAMA #String variable is unchanged.

# Input string doesnt have tobe a alphet only string can contain numbers, special chars etc.
In [12]: strng="sRi RAMA1212#@!"
    ...: print(strng.capitalize())
    ...: print(strng)
    ...:
Sri rama1212#@!
sRi RAMA1212#@!

#Notes: 
#1. Doesn't change the given string by doing inplace operation.
#2. first char is uppercased rest lowercased forcefully.
#3. Input string doesnt have tobe a alphabet only string can contain numbers, special chars etc.

#
#	str.casefold() Returns lowercase version of given string usefull in 
# 					caseless comparison
#
In [11]: strng="sRi RAMA1212#@!" #
    ...: print(strng.casefold())
    ...: print(strng)
    ...:
sri rama1212#@!   
sRi RAMA1212#@!
#Note: Input string doesnt have tobe a alphabet only string can contain numbers, special chars etc.

#
# str.center(width[, fillchar]) #Centers the given string within given width
# str.ljust(width[, fillchar]) -> str
# str.rjust(width[, fillchar]) -> str
#

In [13]: strng="sRi RAMA1212#@!"
    ...: print('|%s|' %strng.center(25))
    ...: print('|'+('----^'*5)+'|')
    ...: print('|%s|' %strng)
    ...:
|     sRi RAMA1212#@!     |
|----^----^----^----^----^|
|sRi RAMA1212#@!|
#
In [34]: print('|'+"Asdas".ljust(20)+'|')
    ...: print('|'+"Asdas".rjust(20)+'|')
    ...: print('|'+"Asdas".center(20)+'|')
    ...:
|Asdas               |
|               Asdas|
|       Asdas        |

#
#str.count(sub[, start[, end]]) 
#	Return the number of non-overlapping occurrences of substring.
#
In [14]: strng="Sri Rama Sri Sita"
    ...: print(strng.count('Sri')) 
    ...: strng="sri Rama Sri Sita" #Both 'sri's are of different case
    ...: print(strng.count('Sri'))
    ...: print((strng.casefold()).count('Sri'.casefold())) #finding no. of occurances of 'sri' of all cases.
    ...:
2
1
2
#	Counts only non overlapping occurances.
In [15]: "adadadada".count('ada')
Out[15]: 2
#Notes: 1. Counts only non overlapping occurances.
#2. canbe used with casefold() to find all occurences of different cases.

#
#	S.endswith(suffix[, start[, end]]) -> bool
#	Return True if S ends with the specified suffix, False otherwise.
#
In [16]: strng="Sri Rama Sri Sita"
    ...: print(strng.endswith('Sita'))
    ...: strng="Sri Rama Sri Sita."
    ...: print(strng.endswith('.'))
    ...:
True
True

#
#S.expandtabs(tabsize=8) -> str
#	Return a copy of S where all tab characters are expanded using spaces.
#
In [18]: strng="Sri\tRama\tSri\tSita"
    ...: print(strng)
    ...: print(strng.expandtabs(1))
    ...: print(strng.expandtabs(4))
    ...:
Sri     Rama    Sri     Sita
Sri Rama Sri Sita
Sri Rama    Sri Sita

#
# S.find(sub[, start[, end]]) -> int
#	Return the lowest index in S where substring sub is found
# S.rfind(sub[, start[, end]]) -> int
#	Return the highest index in S where substring sub is found
#
#
#	S.index(sub[, start[, end]]) -> int #returns lowest index of given substring
#	S.rindex(sub[, start[, end]]) -> int # returns highest index of given substring
#


In [19]: strng="Jai Sri Rama Sri Sita"
    ...: print(strng)
    ...: print(strng.find('Sri'))
    ...: print(strng.find('Sri', 7))
    ...:
Jai Sri Rama Sri Sita
4
13
In [40]: strng="Jai Sri Rama Sri Sita"
    ...: print(strng)
    ...: print(strng.rfind('Sri'))
    ...: print(strng.rfind('Sri', 7))
    ...:
    ...:
Jai Sri Rama Sri Sita
13
13
#Notes:
#1. rfind() & find() returns -1 if substring isnt found.
#2. rindex() & index() will raise "ValueError" if substring isnt found.
#

#
#S.format(*args, **kwargs) -> str
#	Return a formatted version of S, using substitutions from args and kwargs.
#
In [21]: print("Art: {},  Price: {}".format(453, 59.058)) # use {} for replacements
    ...: print("Art: {:5d},  Price: {:8.2f}".format(453, 59.058))# can mention the precision
    ...: print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058)) # can be passed using variable names.
    ...: print("Price: {p:8.2f},  Art: {a:5d}".format(a=453, p=59.058)) # using variable names we can pass args out pf sequence too.
    ...:
Art: 453,  Price: 59.058
Art:   453,  Price:    59.06
Art:   453,  Price:    59.06
Price:    59.06,  Art:   453
#Notes: http://www.python-course.eu/python3_formatted_output.php

#
# S.format_map(mapping) -> str
# 	Return a formatted version of S, using substitutions from mapping.
#
In [22]: my_map={'a':453, 'p':59.058}
    ...: print("Price: {p:8.2f},  Art: {a:5d}".format_map(my_map))
    ...: print('Price: {p},  Art: {a}'.format_map(my_map))
    ...:
Price:    59.06,  Art:   453
Price: 59.058,  Art: 453
#Note: Useful when multiple  lines are to be printed in different formats and dicts


#
#S.isalnum() -> bool
#	Return True if all characters in S are alphanumeric
#
In [25]: print("01203812369123".isalnum())
    ...: print("ABC123".isalnum())
    ...: print("ASBasdas".isalnum())
    ...: print("@#@!@".isalnum())  # Contains non alphanumerics
    ...: print("ABC123@#@!@".isalnum()) # Contains non alphanumerics
    ...:
    ...:
True
True
True
False
False

#
# S.isalpha() -> bool
#		Return True if all characters in S are alphabetic
#

In [26]: print("ASBasdas".isalpha()) 
    ...: print("01203812369123".isalpha()) # Contains non alphabets
    ...: print("ABC123".isalpha())# Contains non alphabets
    ...: print("@#@!@".isalpha())# Contains non alphabets
    ...: print("ABC123@#@!@".isalpha())# Contains non alphabets
    ...:
True
False
False
False
False

#
# S.isdecimal() -> bool
#
In [27]: print("ASBasdas".isdecimal()) # Contains non decimal
    ...: print("01203812369123".isdecimal())
    ...: print("01203812369123.123123".isdecimal())# Contains non decimal
    ...: print("ABC123".isdecimal())# Contains non decimal
    ...: print("@#@!@".isdecimal())# Contains non decimal
    ...: print("ABC123@#@!@".isdecimal())# Contains non decimal
    ...:
False
True
False
False
False
False

#
#S.isdigit() -> bool
#      Return True if all characters in S are digits
#      and there is at least one character in S, False otherwise.
#
In [28]: print("ASBasdas".isdigit())
    ...: print("01203812369123".isdigit())
    ...: print("".isdigit())
    ...: print("01203812369123.123123".isdigit())
    ...: print("ABC123".isdigit())
    ...: print("@#@!@".isdigit())
    ...: print("ABC123@#@!@".isdigit())
    ...:
False
True
False
False
False
False
False

#
#S.isidentifier() -> bool
#      Return True if S is a valid identifier according
#      to the language definition.
#
#       Use keyword.iskeyword() to test for reserved identifiers
#       such as "def" and "class".
# 
""" 
	isidentifier is a Python function that simply tests whether a string
 contains only certain characters (underscore, digits, and alphas) and 
 starts with an alpha or an underscore, so the string can be used for 
 a valid Python identifier. Other functions that test for character 
 classes are isalpha, isalnum, isdigit, and others.
"""
In [29]: ss = (
    ...:     'varABC123',
    ...:     '123ABCvar',
    ...:     '_123ABCvar',
    ...:     'var_ABC_123',
    ...:     'var-ABC-123',
    ...:     'var.ABC.123',
    ...: )
    ...:
    ...: fmt = '%-15s%-10s%-10s%-10s%-10s'
    ...: print(fmt % ('', 'isalpha', 'isalnum', 'isdigit', 'isidentifier'))
    ...: for s in ss:
    ...:     print(fmt % (s, s.isalpha(), s.isalnum(), s.isdigit(), s.isidentifier()))
    ...:
               isalpha   isalnum   isdigit   isidentifier
varABC123      False     True      False     True
123ABCvar      False     True      False     False
_123ABCvar     False     False     False     True
var_ABC_123    False     False     False     True
var-ABC-123    False     False     False     False
var.ABC.123    False     False     False     False

#
#	S.islower() -> bool
#
In [30]: print("asdas".islower())
    ...: print("ASBasdas".islower())
    ...: print("01203812369123".islower())
    ...: print("ABC123".islower())
    ...: print("ABC123@#@!@".islower())
    ...:
True
False
False
False
False
#
# S.isnumeric() -> bool
#
In [31]: print("01203812369123".isnumeric())
    ...: print("0120.3812369123".isnumeric())
    ...: print("ABC123".isnumeric())
    ...: print("ABC123@#@!@".isnumeric())
    ...: print("asdas".isnumeric())
    ...: print("ASBasdas".isnumeric())
    ...:
True
False
False
False
False
False
#
# S.isprintable() -> bool
# S.isspace() -> bool
# S.isupper() -> bool
#

#
#S.istitle() -> bool
'''
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
'''
#
In [32]: print("Asdas".istitle())
    ...: print("Mr.Asdas".istitle())
    ...: print("Mrs.Asdas".istitle())
    ...: print("Lt.Asdas".istitle())
    ...: print("01203812369123".istitle())
    ...: print("0120.3812369123".istitle())
    ...: print("ABC123".istitle())
    ...: print("ABC123@#@!@".istitle())
    ...: print("asdas".istitle())
    ...: print("ASBasdas".istitle())
    ...:
True
True
True
True
False
False
False
False
False
False
#
# S.join(iterable) -> str 
# Join elements of given "iterable" sperating with 'S'
#
In [33]: print("-".join([chr(x) for x in range(ord('a'),ord('z')+1)])) #chr(int) returns "char" equivalent to given ASCII 'int'
    ...: print("-".join([str(x) for x in range(ord('a'),ord('z')+1)])) #str(int) returns "string" equivalent to given 'int' number
    ...:
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z
97-98-99-100-101-102-103-104-105-106-107-108-109-110-111-112-113-114-115-116-117-118-119-120-121-122

#
# S.lower() -> str
# S.upper() -> str
#

In [36]: print("ASBasdaS".lower())
    ...: print("ASBasdaS".upper())
    ...:
asbasdas
ASBASDAS

#
#	S.lstrip([chars]) -> str # remove given chars or whitespaces from left side
#	S.rstrip([chars]) -> str # remove given chars or whitespaces from right side
#	S.strip([chars]) -> str  # remove given chars or whitespaces from both left and right sides
#

In [37]: print('|'+"  ASBasdaS  ".lstrip()+'|')
    ...: print('|'+"  ASBasdaS  ".rstrip()+'|')
    ...: print('|'+"  ASBasdaS  ".strip()+'|')
    ...:
|ASBasdaS  |
|  ASBasdaS|
|ASBasdaS|

#
#	S.partition(sep) -> (head, sep, tail)
'''
 Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
'''
#	S.rpartition(sep) -> (head, sep, tail)
#
In [38]: print("Mr.Asdas".partition('sd'))
    ...:
('Mr.A', 'sd', 'as')
In [39]: print("Mr.Asdas".partition('ad'))
    ...:
('Mr.Asdas', '', '')
#
In [42]: print(strng.partition('Sri'))
    ...: print(strng.rpartition('Sri'))
    ...:
('Jai ', 'Sri', ' Rama Sri Sita')
('Jai Sri Rama ', 'Sri', ' Sita')

#
#	S.rsplit(sep=None, maxsplit=-1) -> list of strings
#
In [43]: print('OmRama JaiRama SriRama'.rsplit())
    ...: print('OmRama JaiRama SriRama'.split())
    ...:
['OmRama', 'JaiRama', 'SriRama']
['OmRama', 'JaiRama', 'SriRama']

In [44]: print('OmRama JaiRama SriRama JaiJaiRama'.rsplit(" ",1))
    ...: print('OmRama JaiRama SriRama JaiJaiRama'.split(" ",1))
    ...:
['OmRama JaiRama SriRama', 'JaiJaiRama']
['OmRama', 'JaiRama SriRama JaiJaiRama']
# Notes: In the absence of "maxsplit" split&rsplit works same

#
# S.splitlines([keepends]) -> list of strings
#
In [45]: print("""OmRama JaiRama SriRama JaiJaiRama
    ...: Sri Sita JaiSita JaiJai Sita
    ...: Sri Hanuman JaiHanuman JaiJaiHanuman""".splitlines())
    ...:
['OmRama JaiRama SriRama JaiJaiRama', 'Sri Sita JaiSita JaiJai Sita', 'Sri Hanuman JaiHanuman JaiJaiHanuman']

#
# S.swapcase() -> str
#
In [46]: print('OmRama JaiRama SriRama JaiJaiRama'.swapcase())
oMrAMA jAIrAMA sRIrAMA jAIjAIrAMA

#
# S.title() -> str
#
In [47]: print('omRama JaiRama SriRama JaiJaiRama'.title())
Omrama Jairama Srirama Jaijairama

#
# S.startswith(prefix[, start[, end]]) -> bool
#
In [48]: print('OmRama JaiRama SriRama JaiJaiRama'.startswith('Om'))
    ...: print('OmRama JaiRama SriRama JaiJaiRama'.startswith('Jai',7))
    ...: print('OmRama JaiRama SriRama JaiJaiRama'.startswith(('Om','Jai','Sri')))
    ...:
True
True
True
#Note: Prefix can be a string or tuple of trings to try with

#
#  S.translate(table) -> str
#	Return a copy of the string S in which each character has been mapped
#   through the given translation table.
#

#creation of translation Table
In [54]: str.maketrans('Rama','Sita')
Out[54]: {82: 83, 97: 97, 109: 116}

#
In [53]: print('OmRama JaiRama SriRama JaiJaiRama'.translate(str.maketrans('Rama','Sita')))
    ...:
OtSata JaiSata SriSata JaiJaiSata

#
#  S.zfill(width) -> str #Pad a numeric string S with zeros on the left,
#
In [56]: print("omrama".zfill(10))
    ...: print("omrama".zfill(1)) #Doesnt truncate the word
    ...:
0000omrama
omrama

###########################################################################
#
# range() only takes int as args if you want to give range of char use ord(char) ascii values
#

#
#for...else
#
for x in range(1505, 1540):
	if (x%7==0 and x%5==0):
		print(x, end=" ")
		break
else:
	print("No number found as such!!")
#
number=(1, 2, 3, 4, 5, 6, 7, 8, 9) 
print("Total evens: ",len([i for i in number if(i%2==0)]))
print("Total odds: ",len([i for i in number if(i%2!=0)]))
#
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
print(*[(x,type(x)) for x in datalist])
#
# Create 2D array with a formula

Rows=3
Cols=4
print([[i*j for j in range(Cols)]  for i in range(Rows)])
#
In [25]: for x in range(6,-1,-1):
    ...:     print(x,end=" ")
    ...:
6 5 4 3 2 1 0
#
print(*[x for x in range(1505, 2701)	if (x%7==0 and x%5==0)])
#

#
# Lambda
#
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

data_list = input("Input a string")
print(len(list(filter(lambda x: x.isdigit(), data_list))))
print(len(list(filter(lambda x: x.isalpha(), data_list))))
#Note: filter returns an object but not an iterable

#
# Class
#
#Srimatrenamaha!
class student:
	name=""
	def getname(self):
		print(self.name)

var=student()
var.name="Srirama"
print(id(var.getname()))
var2=student()
var2.name="SriSitarama"
print(id(var2.getname()))
#
#if else
#
astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
###


#
# Logic implementations
#
def isleapyear(year):
	if(( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
		return True
	else:
		return False

print(isleapyear(2000))
print(isleapyear(2004))
print(isleapyear(1900))
print(isleapyear(1600))
####

In [7]: sys.getrecursionlimit()
Out[7]: 1000

def max_n(mylist):
	if( len(mylist) > 2 ):
		return( max_n( (mylist[0], max_n(mylist[1:])) ) )
	else:
		if( mylist[0] > mylist[1] ):
			return mylist[0]
		else:
			return mylist[1]

print(max_n((1000,-2000,30000,-20,200)))

def max_n_nonrecursive(mylist):
	temp=mylist[0]
	for i in mylist:
		if temp < i:
			temp=i
	return(temp)

print(max_n_nonrecursive( [x for x in range(1999999)] ))
#
# sum of a list
#
def allsum(mylist):
	mysum=0
	for i in mylist:
		mysum+=i
	return (mysum)

def allsum_recursive(mylist):
	if len(mylist) == 1:
		return mylist[0]
		
	return(mylist[0]+allsum_recursive(mylist[1:]))
	
	
print(allsum_recursive((8, 2, 3, 0, 7)))
#
# Factorial / sum of items of a list
# 
def allsum(mylist):
	mysum=1
	for i in mylist:
		mysum*=i
	return (mysum)

def allsum_recursive(mylist):
	if len(mylist) == 1:
		return mylist[0]
		
	return(mylist[0]*allsum_recursive(mylist[1:]))
	
	
print(allsum_recursive([x for x in range(1,999)]))
#
def factorial(number):
	if number == 0:
		return 1
	return (number*factorial(number-1) )

def allproduct_recursive(mylist):
	if len(mylist) == 1:
		return mylist[0]
		
	return(mylist[0]*allproduct_recursive(mylist[1:]))
	
number=100
fact1=factorial(number)
fact2=allproduct_recursive([x for x in range(1,number+1)])

if (fact1 == fact2):
	print("Both are same: \n %d" %fact1)
else:
	print("Something went wrong!")



#
# string reverse using recursive
#

def str_rev_recusive(string):
	if(len(string) == 1):
		return string[0]
	return(str_rev_recusive(string[1:])+string[0])
		
string="SriRamaJayamu"
print(string)
print(str_rev_recusive(string))


#
# Difference between .sort and sorted()
#
mylist=[a,b,c,23,44,27,45]
mylist.sort() #inplace sort
print(mylist)
mysorted=sorted(mylist) # returns a sorted one
print(mysorted)

