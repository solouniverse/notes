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

