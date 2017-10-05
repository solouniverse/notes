
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
