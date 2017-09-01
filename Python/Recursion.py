
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

