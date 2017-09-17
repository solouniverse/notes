"""
 * Palindrome Permutation:
 * Ex: i/p tact cao
 * "taco cat", "atco cta"
 * 
"""
import collections

strng="aaaaaaabbc"
strng_len=len(strng)
count=collections.Counter(strng)
print(count)

odd_count=0

for val_count in count.values():
	if(val_count%2):
		if odd_count:
			break
		odd_count+=1

if (odd_count and not strng_len%2) or (odd_count > 1):
	print("Not a polindrome")
else:
	print("'%s' a polindrome" %strng)
print(odd_count)
