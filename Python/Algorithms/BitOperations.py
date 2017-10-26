
def get_first_1_in_number(number):
	count=0
	mask=1
	while(number >= mask):
		count+=1
		if(number & mask != 0):
			break
		mask=mask<<1
		print(bin(mask))
	print("Found first '1' at : ", count)

	count=0
	while(number!=0):
		count+=1
		if(number & 1 != 0):
			break
		number=number>>1
		print(bin(number))
	print("\n---------------------\nFound first '1' at : ", count, number)

#get_first_1_in_number(number)
#exit()
def FindFirstDiffBit():
	M=52
	N=4
	mask=1
	count=0
	found_diff=0
	while(mask < 1<<32):
		count+=1
		if((M ^ N)& mask):
			found_diff=count
			break
		mask=mask<<1
	print("Found first difference at : ", found_diff)

def CheckKthBit():
	number=1024
	K=11
	if(number & 1<<(K-1)):
		print("Yes")
	else:
		print("No")
		
def  CheckPerfect2PowX():
	number=1024
	if(number & (number-1) == 0):
		print("Its a perfect 2^x")
	else:
		print("Its **NOT** a perfect 2^x")

def FindDifferentBits():
	A=1023
	B=11
	print(bin(A))
	print(bin(B))
	mask=1
	diffcount=0
	while(mask < A or mask < B):
		if((A^B) & mask):
			diffcount+=1
		mask=mask<<1
	print("Total Number of different bits: ", diffcount)

#print(bin((((5<<4) + 5)<<8)+(5<<4) + 5))
def InterchangeEvenOddBits():
	mask=5
	A=23
	count=4
	while(mask < A):
		mask=mask+(mask<<(count))
		count*=2

	print(bin(mask))
	print(bin(A))
	print(bin(A&mask))
	print(bin(A&(mask<<1)))
	print(bin((A&(mask<<1))<<2))
	print(bin(((A&(mask<<1))<<2)|(A&mask)) )
	print((((A&(mask<<1))<<2)|(A&mask)) )
	print(bin(((A&(mask<<1)))|(A&mask)<<2) )
	print((((A&(mask<<1)))|(A&mask)<<2)>>1)

def createAlternateBitMask():
	mask=5
	A=1023
	while(mask < A):
		print(bin(mask))
		mask=5+(mask<<4)

	print(bin(mask))

def isNumberSparse(number):
#Given a number, check whether it is sparse or not. A number is said to be a sparse number if in binary representation of the number no two or more consecutive bits are set.
	return(number&(number<<1))

def count_number_of_set_bits(n=51):
	count=0
	print(bin(n))
	while(n):
		n&=(n-1)
		count+=1

	print(count)

count_number_of_set_bits()
