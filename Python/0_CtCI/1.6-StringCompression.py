"""
//SriMatreNamaha!
 * Implement a method to perform basic string compression using the 
 * 		counts of repeated characters.
 * Ex:
 * 		aaabbbccc -> a3b3c3
 * 		aaaaaaaaaaaabbaaabbaaaaabac -> a12b2a3b2a5b1a1c1
 * 
"""
String="aaaaaaaaaaaabbaaabbaaaaabac"
String="abbbbcc"
compressed=""
count=1
for j in range(len(String)):
	print(j,String[j],compressed,count)
	try:
		if(String[j+1] == String[j]):
			count+=1
		else:
			compressed+=String[j]+str(count)
			count=1
	except:
		compressed+=String[j]+str(count)

print(compressed)

"""

str1="aaaabbbcccaaabbccccc"
value=str1[0]
str2=""
count=0
for i in str1:
	if i == value:
		count+=1
	else:
		str2=str2+value+str(count)
		value=i
		count=1

str2=str2+value+str(count)

print(str2)
"""













