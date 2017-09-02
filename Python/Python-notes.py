#SrimatreNamaha!
#
# range() only takes int as args if you want to give range of char use ord(char) ascii values
#
In [2]: print(*[ chr(c) for c in range(ord('A'), ord('Z')+1)])
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

In [3]: print(*[ chr(c) for c in range(ord('a'), ord('z')+1)])
a b c d e f g h i j k l m n o p q r s t u v w x y z

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
# Difference between .sort and sorted()
#
mylist=[a,b,c,23,44,27,45]
mylist.sort() #inplace sort
print(mylist)
mysorted=sorted(mylist) # returns a sorted one
print(mysorted)

