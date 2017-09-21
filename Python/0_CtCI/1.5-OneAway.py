"""
1. check length
2. check sets True false!
3. check each char now!
	a. if any char has more than 1 count difference -> false
	b. if more than 1 char has more than 1 count difference -> false
"""
import collections

def OneEditAway(string1,string2):
""" This logic has a big flaw!! """		
	missing_chars=0
	OneDiffer=0
	if(len(string1) < len(string2)):
		string1, string2 = string2, string1

	string1_counter=collections.Counter(string1)
	string2_counter=collections.Counter(string2)

	for char, count in string1_counter.items():
		try:
			if (string2_counter[char]-count in (-1,1)):
				print("more than 1 count different with:",char)
				if(OneDiffer == 1):
					print("More than 1 char has more than 1 count difference:")
					return False
				OneDiffer+=1
			if (string2_counter[char]-count not in (-1,0,1)):
				print("more than 1 count difference")
				return False
		except:
			missing_chars+=1
			if(missing_chars >1):
				print("Morethan 1 missing chars found")
				return False

	if(OneDiffer == 1):
		return True
	else:
		return False

string1="paesode"
string2="mpaesode"

if(len(string1) < len(string2)):
	string1, string2 = string2, string1
	
def OneEditAway_2(string1,string2): 
""" This Logic doesn't work """	
	j=0
	missingChar=0
	for i in range(len(string1)):
		try:
			if(string1[i] == string2[j]):
				j+=1
			else:
				if(string1[i+1] == string2[j+1]):
					j+=1
					missingChar+=1
				elif(string1[i+1] == string2[j]):
					missingChar+=1
									
				if(abs(i-j) not in (1,0)) or missingChar >1:
					print(" False",missingChar,i,j)
					break
					
		except IndexError:
			if (j>=len(string2)):
				i+=1
			
	else:
		print(" True ")

def OneEditAway_3(string1,string2): 
"""Working Logic"""	
	j=0
	for i in range(len(string1)):
		try:
			if(string1[i] == string2[j]):
				j+=1
			else:
				if(string1[i+1:] == string2[j+1:]) or (string1[i+1:] == string2[j:]):
					print("From 1")
					return (True)
				else:
					return (False)
					
		except IndexError:
			print("caught IndexError")

	else:
		print("From 2")
		return True	

if(OneEditAway_3(string1,string2)):
	print("1 Char edit Away!!")
else:
	print("Its **NOT**!!")
	
