"""

1. check length
2. check sets True false!
3. check each char now!
	a. if any char has more than 1 count difference -> false
	b. if more than 1 char has more than 1 count difference -> false
"""
import collections

def OneAway(string1,string2):
		
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

string1="palesde"
string2="palesd"

if(OneAway(string1,string2)):
	print("1 Char edit Away!!")
else:
	print("Its **NOT**!!")
	
