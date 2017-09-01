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

