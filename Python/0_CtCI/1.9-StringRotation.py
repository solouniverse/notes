string1="abcdaef"
string2="fabcdae"

tempString=string2*2

"""
print(set(string1.split(string1[1])))
print(set(tempString.split(string1[1])))
#This logic doesnt work
if(sorted(string1.split(string1[0])) == sorted(string2.split(string1[0]))):
"""
#if string1 in tempString:
#if len(tempString.split(string1))>1:
if tempString.find(string1) != -1:
	print("Yes")
else:
	print("No")

