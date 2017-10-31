str1=yqtwueytqwejyvsjhfdasdfisdfblkaasfudasdoiqwer =n
str2=aeiou =m

def solution_1():
#O(n*m) O(2N)
	i=0
	for x in range(len(str1)):
		for y in  range(len(str2)):
			if x==y:
				break
		else:
			str3[i]=x
			i+=1
		
				
def solution_2():
#O(n*n*m) O(N)
	i=0
	x=0
	str_len=len(str1):
	while(x<str_len):
		for y in  range(len(str2)):
			if str1[x]==str2[y]:
				for z in range(x,str_len)
					str1[z]=str1[z+1]
				
				str_len-=1
				x-=1
				break
		x+=1

def solution_3():
#O(n*n-(no.matching-1)*m) O(N)
	i=0
	str_len=len(str1):
	x=str_len
		
	while(x>-1):
		for y in  range(len(str2)):
			if str1[x]==str2[y]:
				for z in range(x,str_len)
					str1[z]=str1[z+1]
				
				str_len-=1
				break
		x-=1

def solution_4():
#O(n) O(N)
	i=0
	str_len=len(str1):
	x=str_len
	str2=[] #27
	for x in range(ord('z')+1-ord('a'))
		if chr(x+ord('a')) in 'aeiou':
			str2[x]=1
		else:
			str2[x]=0
	while(x>-1):
		#for y in  range(len(str2)):
		if (str2[str1[x]-ord('a')]):
			for z in range(x,str_len)
				str1[z]=str1[z+1]
			
			str_len-=1
			break
		x-=1

66,66+27


	c
if(str2[ord(c)-ord('a')]): #O(1)
	
m


----

#AB BA
#ABC: ABC ACB BCA BAC CAB CBA
# Find Permutations of a string
def CircularRotateBy1Char(string):
	return(string[1:]+string[0])

def get_permutations(string):
	print(CircularRotateBy1Char("string"))
	string="ABC"
	TempString=CircularRotateBy1Char(string)
	print(TempString)
		
	while(string != TempString):
		TempString=CircularRotateBy1Char(TempString)
		#while(i>2):
			
		print(TempString)


string= "ABCD"

for x in string:
	for y in string.replace(x,''):
		print(x+y)
#
#swapCharCase
#
def swapCharCase(c):
#	if((ord(c) >= ord('A')) and (ord(c) <=ord('Z'))):
#	if(ord(c) in range(ord('A'), ord('Z')+1)):
	if(ord('Z') >= ord(c) >=ord('A')):
		return chr(ord('a')-ord('A')+ord(c))
	elif(ord(c) in range(ord('a'), ord('z')+1)):
		return chr(ord('A')-ord('a')+ord(c))
	else:
		return c
def swapCase(string):
	SwappedString=""
	for x in string:
		SwappedString+=swapCharCase(x)
	return SwappedString

string="stringStRiNg1231^*&^!@WS+_-"

print(string)
print(swapCase(string))
#
# Write a function to convert a string into an integer.  
#
def convertStrinToInt(NumString):
	Number=0
	for x in NumString:
		#print(Number)
		if('0' <= x <= '9'):
			Number=Number*10+ ord(x) - ord('0')
		else:
			raise TypeError
	return(Number)

NumString="12s34"	
Number=convertStrinToInt(NumString)
print(Number)
print(type(Number))
