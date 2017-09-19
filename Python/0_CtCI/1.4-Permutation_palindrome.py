"""
 * Palindrome Permutation:
 * Ex: i/p tact cao
 * "taco cat", "atco cta"
 * 
"""
import collections

def isPermutation_of_Palindrome_methon2(string):
	strng_len=len(strng)
	count=collections.Counter(strng)
	odd_count=0

	for val_count in count.values():
		if(val_count%2):
			odd_count+=1
			if odd_count>1:
				break

	if (odd_count and not strng_len%2) or (odd_count > 1):
		return False
	else:
		return True

def isPermutation_of_Palindrome_v1(string):
	repetitions=collections.Counter(string)
	lenght=len(string)
	Permutation_of_Palindrome=1
	oddCount=0

	if(lenght%2 == 0):
		for values in repetitions.values():
			if values%2 != 0:
				Permutation_of_Palindrome=0
				break
	else:
		for values in repetitions.values():
			if values%2 != 0:
				oddCount+=1

	if ((Permutation_of_Palindrome) and (lenght%2 == 0)) or (oddCount==1):
		return True
	else:
		return False

def isPermutation_of_Palindrome_v2(string):
	repetitions=collections.Counter(string)
	lenght=len(string)
	oddCount=0

	if(lenght%2 == 0):
		for values in repetitions.values():
			if values%2 != 0:
				return False
		return True
	else:
		for values in repetitions.values():
			if values%2 != 0:
				oddCount+=1

	if oddCount != 1:
		return False
	else:
		return True
		
#This logic failes when even number of odd occurances are found in even string
def isPermutation_of_Palindrome_v3(string):
	repetitions=collections.Counter(string)
	lenght=len(string)
	oddCount=0

	if(lenght%2 == 0):
		if(sum(repetitions.values())%2 != 0):
			return False
		return True
	else:
		for values in repetitions.values():
			if values%2 != 0:
				oddCount+=1

	if oddCount != 1:
		return False
	else:
		return True


string="aabbcc"

if (string != ""):
	if (isPermutation_of_Palindrome(string)):
		print("Its a Permutation of Palindrome!!")
	else:
		print("Its **NOT** a Permutation of Palindrome")
else:
	print("Zero length string!")

