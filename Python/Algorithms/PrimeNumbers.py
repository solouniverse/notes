def isPrimeRegular(n):
#O(n)
	count=0
	for i in range(2,n):
		count+=1
		if(n%i == 0):
			return [False, count]

	#print(i, end=":")
	return [True, count]
			
def isPrimeOptimal(n):
#O(n^0.5)
	count=0
	for i in range(2,n):
		count+=1
		if(n%i == 0):
			return [False, count]
# Check only upto SQRT(n) but not until 'n-1'
		if(i*i>=n):
			break
	#print(i, end=":")
	return [True, count]

def FindPrimesInRange(n,numList):
#O(n*n*n)+list.remove() overhead of size 'n'
#Works on a list of numbers upto range 'n' by removing non-primes
#
#Any number can be represented by prime factors	upto it
#Take the range of number upto 'n' and remove those which are not primes.
#Use earlier prime numbers to check primality of a number
#
	numListLength=len(numList)
	i=1
	count=0
	while(1):
		if(i>=numListLength):
			break
		for j in range(i):
			count+=1
			if(numList[i]%numList[j]==0):
				numList.remove(numList[i])
				count+=numListLength-i
				i-=1
				numListLength-=1
				break

		i+=1
	print("count: ", count)
	return (numList)

def FindPrimesInRangeV2(n, numList):
#O(n*n)
#Works on a list of numbers upto range 'n' by removing non-primes **w/o list.remove overhead**
#**Implemented own list.remove() using 2 indices reduced exe time by 50%
#
#Any number can be represented by prime factors	upto it
#Take the range of number upto 'n' and remove those which are not primes.
#Use earlier prime numbers to check primality of a number
#
	numListLength=len(numList)
	numListLength2=numListLength
	i=1
	k=1
	count=0
	while(1):
		if(i>=numListLength or k>=numListLength2-1):
			break
		for j in range(i):
			count+=1
			if(numList[i]%numList[j]==0):
				#numList.remove(numList[i])
				i-=1
				numListLength-=1
				break

		i+=1
		k+=1
#Implement own list.remove() to reduce the exec time and it works !!
		if(k!=i):
			numList[i]=numList[k]
	print("count: ", count)
	return (numList[:numListLength])

def FindPrimesInRangeV3(n):
#** Prepare a list of primes by adding numbers to list if they qualify the condition(See if there are no prime factors upto it).
#(But not by removing non-primes from prepared list of n numbers. So no overhead of managing huge list)
#
#Any number can be represented by prime factors	upto it.
#Use earlier prime numbers to check primality of a number
#
	PrimeList=[2]
	count=0
	for x in range(3,n+1):
		for y in PrimeList:
			if x%y==0:
				count+=1
				break
		else:
			PrimeList.append(x)
	print("count: ", count)
	return PrimeList

def FindPrimesInRangeV4(n):
#** Prepare a list of primes by adding numbers to list if they qualify the condition
#(See if there are no prime factors upto **sqrt(n)** only but not primes upto it).
#(But not by removing non-primes from prepared list of n numbers)
#
#Any number can be represented by prime factors	upto it.
#Use earlier prime numbers to check primality of a number
	PrimeList=[2]
	count=0
	for x in range(3,n+1):
		for y in PrimeList:
			if x%y==0:
				count+=1
				break
			if(y*y>=x):
				PrimeList.append(x)
				break
		else:
			PrimeList.append(x)
	print("count: ", count)
	return PrimeList

def FindPrimesInRangeRegular(n):
# A bruteforce method of finding primes: check factors till n-1
# O(n^2)
	PrimeList=[2]
	count=0
	for _ in range(3,n+1):
#O(n)
		for i in range(2,_):
			count+=1
			if(_%i == 0):
				break
		else:
			PrimeList.append(_)
		
	print("count: ", count)
	return PrimeList

def FindPrimesInRangeSqrt(n):
# O(n*sqrt(n))
# Check factors only upto **sqrt(n)** but not till n-1
# A bit better than bruteforce method of finding primes
	PrimeList=[2]
	count=0
	for _ in range(3,n+1):
		#O(n^0.5)
		for i in range(2,_):
			count+=1
			if(_%i == 0):
				break
	# Check only upto SQRT(n) but not until 'n-1'
			if(i*i>=_):
				PrimeList.append(_)
				break
	print("count: ", count)
	return(PrimeList)	

def FindPrimesInRangeV4_2(mylist):
	PrimeList=[2]
	count=0
	prev=mylist[0]
	for n in mylist:
		for x in range(prev,n+1):
			for y in PrimeList:
				if x%y==0:
					count+=1
					break
				if(y*y>=x):
					PrimeList.append(x)
					break
			else:
				PrimeList.append(x)
		print("count: ", count)
		print(len(PrimeList))
		prev=n


#mylist=[3,10,31,100,316,1000,3162,10000,31622,100000,316227,1000000,3162277,10000000,31622776,100000000,316227766,1000000000,3162277660,10000000000,31622776601,100000000000,316227766016,1000000000000,3162277660168,10000000000000]
#FindPrimesInRangeV4_2(mylist)
#exit()
#for n in mylist:
#	print(len(FindPrimesInRangeV4(n)))
#exit()
n=1000001

import cProfile
print("FindPrimesInRangeRegular(%d):-----" %n)
cProfile.run("FindPrimesInRangeRegular(n)")
print("FindPrimesInRangeSqrt(%d):-----" %n)
cProfile.run("FindPrimesInRangeSqrt(n)")
print("FindPrimesInRange(%d):-----" %n)
numList=[x for x in range(2, n)]
cProfile.run("FindPrimesInRange(n,numList)")
print("FindPrimesInRangeV2(%d):-----" %n)
numList=[x for x in range(2, n)]
cProfile.run("FindPrimesInRangeV2(n,numList)")
print("FindPrimesInRangeV3(%d):-----" %n)
cProfile.run("FindPrimesInRangeV3(n)")
print("FindPrimesInRangeV4(%d):-----" %n)
cProfile.run("FindPrimesInRangeV4(n)")

"""
FindPrimesInRangeRegular(100001):-----
count:  455189160
         9596 function calls in 49.023 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   49.023   49.023 <string>:1(<module>)
        1   49.022   49.022   49.023   49.023 PrimeNumbers.py:125(FindPrimesInRangeRegular)
        1    0.000    0.000   49.023   49.023 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     9591    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


FindPrimesInRangeSqrt(100001):-----
count:  2755295
         9596 function calls in 0.472 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.472    0.472 <string>:1(<module>)
        1    0.472    0.472    0.472    0.472 PrimeNumbers.py:142(FindPrimesInRangeSqrt)
        1    0.000    0.000    0.472    0.472 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     9591    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


FindPrimesInRange(100001):-----
count:  4541451422
         90413 function calls in 18.995 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   18.995   18.995 <string>:1(<module>)
        1    8.893    8.893   18.995   18.995 PrimeNumbers.py:25(FindPrimesInRange)
        1    0.000    0.000   18.995   18.995 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    90407   10.101    0.000   10.101    0.000 {method 'remove' of 'list' objects}


FindPrimesInRangeV2(100001):-----
count:  46314476
         6 function calls in 8.412 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.412    8.412 <string>:1(<module>)
        1    8.412    8.412    8.412    8.412 PrimeNumbers.py:53(FindPrimesInRangeV2)
        1    0.000    0.000    8.412    8.412 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


FindPrimesInRangeV3(100001):-----
count:  90408
         9596 function calls in 2.948 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.948    2.948 <string>:1(<module>)
        1    2.946    2.946    2.947    2.947 PrimeNumbers.py:85(FindPrimesInRangeV3)
        1    0.000    0.000    2.948    2.948 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     9591    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


FindPrimesInRangeV4(100001):-----
count:  90408
         9596 function calls in 0.091 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.090    0.090 <string>:1(<module>)
        1    0.090    0.090    0.090    0.090 PrimeNumbers.py:104(FindPrimesInRangeV4)
        1    0.000    0.000    0.091    0.091 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     9591    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
