"""
 * Implement an algorithm to determine if a string has all unique 
 * characters. What if you cannot use additional datastructes?
 *  
"""
 
import cProfile

def using_sets(string):	
	if(len(string) != len(set(string))):
		print("Not Unique")
	else:
		print("Its Unique!")

def using_Counter(string):
	import collections
	for x in (collections.Counter(string)).values():
		if x > 1:
			print("Not Unique")
			break
	else:
		print("Its Unique!")	

def using_str_count(string):
	for x in string:
		if string.count(x) > 1:
			print("Not Unique")
			break
	else:
		print("Its Unique!")	

def using_extra_string(string):
	newString=""
	for x in string:
		if x not in newString:
			newString+=x
		else:
			print("Not Unique")
			break
	else:
		print("Its Unique!")

def using_each_char_vs_rest_of_the_string(string):
	for i in range(len(string)):
		if string[i] in string[i+1:]:
			print("Not Unique")
			break
	else:
		print("Its Unique!")	

string="qwertyuiopasdfghjklzxcvbnm,/.1234567890-=_+!@#$%^&*(:'"
using_sets(string)
using_Counter(string)
using_str_count(string)	
using_extra_string(string)
using_each_char_vs_rest_of_the_string(string)
