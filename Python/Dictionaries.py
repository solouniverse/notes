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

