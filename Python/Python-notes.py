#SrimatreNamaha!
# Pending list
try except
unittest & mock
study one module.py 100%


#
# range() only takes int as args if you want to give range of char use ord(char) ascii values
#
In [2]: print(*[ chr(c) for c in range(ord('A'), ord('Z')+1)])
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

In [3]: print(*[ chr(c) for c in range(ord('a'), ord('z')+1)])
a b c d e f g h i j k l m n o p q r s t u v w x y z

#
# for...else
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
#
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
#### Logic implementations
#
# parenthese
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for  in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))

# prime numbers
def isprime(n):
	for i in range(2,n):
		if n%i == 0:
			break
	else:
		return True
	return False

m=20
print(*[n for n in range(2,m) if isprime(n)])
print(*filter(lambda n: isprime(n), [n for n in range(2,m)]))
print(*filter(isprime, [n for n in range(2,m)]))

#perfect number
#for n in range(1,101):
n=6
print("%d is a perfect number" %n) if( sum([x for x in range(1,n) if n%x == 0]) == n) else print("", end ="") 
"""
def isperfect (n) :
	if(sum([x for x in range(1,n) if n%x == 0]) == n):
		return True 
	else:
		return False
print(isperfect(6))

#
#print(*filter(isperfect, [n for n in range(1,1010)] ) )
#print(*filter(lambda n : if(sum([x for x in range(1,n) if n%x == 0]) == n), [n for n in range(1,1010)] ) )
#print(*filter(lambda n: if sum([x for x in range(1,n) if n%x == 0]) == n , [m for m in range(1,1010)]))
#print(*filter(lambda n: True , [m for m in range(1,1010)]))
"""
#pascal Triangle
In [50]: rows=6
    ...: mylist=[1]
    ...: for x in range(rows):
    ...:     print(mylist)
    ...:     mylist=[mylist[y]+mylist[y+1] for y in range(len(mylist)-1)]
    ...:     mylist.extend([1])
    ...:     mylist[1:]=mylist
    ...:     mylist[0]=1
    ...:
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
#2
rows=6
mylist=[1]
for x in range(rows):
	print(mylist)
	mylist=[mylist[y]+mylist[y+1] for y in range(len(mylist)-1)]
	mylist.insert(0,1)
	mylist.append(1)

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):  # Its a way to filter out _ve numbers
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1	# return False if its a negative number
pascal_triangle(6)
#
#binary_search
#
def binary_search(mylist, element):
	low = 0
	high = len(mylist) -1
	while (low < high):
		mid= (low+high)//2
		print(low,high,mid)
		if (mylist[mid] > element):
			high=mid-1
		elif (mylist[mid] < element):
			low=mid+1
		else:
			print("Found %d @ %d index" %(element, mid))
			return (mid)
		if low==high:
			return -1
	return (-1 )
#
# bubbleSort
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)		
#
# selectionSort
#
def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos]
       nlist[maxpos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)
#
# Convert int to string in any base
#
def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,16))
#
# GCD
#
def Recurgcd(a, b):
	print(a, b)
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return Recurgcd(low, high%low)
print(Recurgcd(12,24))

#
# nth fib using recursion
#
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

print(fibonacci(7))
#
# insertionSort
#
def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)
#
# pangram
string="The quick brown fox jumps over the lazy dog"
string=string.casefold()
string=set(string)

if (len(string) == 27 and " " in string) or (len(string) == 26 and " " not in string):
	print("Its A pangram")
else:
	print("Its not a pangram")
#or
for i in range(ord('a'), ord('z')+1):
	if chr(i) not in "The quick brown fox jumps over the lazy dog".casefold():
		print("Its not a pangram")
		break
else:
	print("Its A pangram")

#or
string="The quick brown fox jumps over the lazy dog"
string=string.casefold()
string_set=set(string)
alphabets=set([chr(i) for i in range(ord('a'), ord('z')+1)])
print("Its a pangram") if (string_set.issuperset(alphabets)) else print("Its not a pangram")
#
#Combinations of character 
#
my_list= [4, 5, 6]
#my_list=set(my_list)

def subsetsRecur(current, sset):
	if sset:
		print(current, sset[1:],")(",current + [sset[0]], sset[1:])
		#print("> ",current, sset)
		return subsetsRecur(current, sset[1:]) + subsetsRecur(current + [sset[0]], sset[1:])
	return [current]

print(my_list)
print(subsetsRecur([],my_list))


#
# Execute string as code
#
mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""
exec(mycode)
exec(code)
#
# Calling functions insidea function
#
In [51]: def fun1(a):
    ...:     def fun2():
    ...:         nonlocal a
    ...:         print(a)
    ...:         a=a+" end"
    ...:         return a
    ...:     fun2()
    ...:     print(a)
    ...:     return 0
    ...: fun1("ABC")
    ...:
ABC
ABC end
Out[51]: 0

#or

In [52]: def fun1(a):
    ...:     def fun2():
    ...:         return a+" end"
    ...:
    ...:     return "start "+fun2()
    ...: print(fun1("ABC"))
    ...:
start ABC end
#or
In [53]: def fun1(a):
    ...:     def fun2(b):
    ...:         return b+" end"
    ...:
    ...:     return "start "+fun2(a)
    ...: print(fun1("ABC"))
    ...:
start ABC end
#
# Number of local variables
#
def abc():
    x = 1
    y = 2
    str1= "w3resource"

print(abc.__code__.co_nlocals)
#
# Providing runtime formatting length
#
from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

max_len = 0

for data in Country:
	if len(data.name) > max_len:
		max_len = len(data.name)
		
for data in Country:
    print('{:{}} = {}'.format(data.name,max_len+12, data.value))

#
# sort enums based on values
#

	
print(sorted([ data.value for data in Country]))
print(list(map(int, Country))
#
# Queue
#
import queue
q = queue.LifoQueue() 
q = queue.Queue() #FIFO Q
#insert items at the head of the queue 
for x in range(4):
    q.put(str(x))
#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print()
#Notes:
# list(q.queue) return list with items in Q



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
# get the class of object
#
mycircle=circle(1)
print(type(mycircle).__name__)

#
#if else
#
astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
###

#
# for loop without using iterate variable (i)
#

for _ in range(5):
	print("asdasd")

#
# Difference between .sort and sorted()
#
mylist=[a,b,c,23,44,27,45]
mylist.sort() #inplace sort
print(mylist)
mysorted=sorted(mylist) # returns a sorted one
print(mysorted)

#
#IMP links
#
http://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
http://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php

https://docs.python.org/3/library/2to3.html
https://docs.python.org/3/library/unittest.mock.html
https://docs.python.org/3/library/unittest.html

#
# Arrays:
#

from array import *
array_num = array('i', [1,3,5,7,9])
print([i for i in array_num])
array_num.append(11)
print([i for i in array_num])
array_num.append([12,13,14]) # is not supported will raise "TypeError: an integer is required (got type list)"
print([i for i in array_num])
print(array_num.itemsize)   # bytes allocated for each element
#
#Numpy
#
In [17]: import numpy as np
    ...: l = [12.23, 13.32, 100, 36.32]
    ...: print("Original List:",l)
    ...: a = np.array(l)
    ...:
    ...: print("One-dimensional numpy array: ",a)
    ...:
    ...:
Original List: [12.23, 13.32, 100, 36.32]
One-dimensional numpy array:  [  12.23   13.32  100.     36.32]

In [18]: import numpy as np
    ...: l = [12.23, 'c',13.32, 100, 36.32]
    ...: print("Original List:",l)
    ...: a = np.array(l)
    ...:
    ...: print("One-dimensional numpy array: ",a)
    ...:
    ...:
Original List: [12.23, 'c', 13.32, 100, 36.32]
One-dimensional numpy array:  ['12.23' 'c' '13.32' '100' '36.32']
#
# scope of variables
#
dir() will give you the list of in scope variables:
globals() will give you a dictionary of global variables
locals() will give you a dictionary of local variables
