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

def FindPrimesInRange(n):
#O(n*n*n)
	numList=[x for x in range(2, n)]
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

def FindPrimesInRangeV2(n):
#O(n*n)
	numList=[x for x in range(2, n)]
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

def FindPrimesInRangeRegular(n):
	#PrimeList=filter(lambda x: isPrimeRegular(x), [ _ for _ in range(3,n)])
	#print(*PrimeList)
	#return
	count=0
	for _ in range(3,n):
		count+=isPrimeRegular(_)[1]
		#print(_, isPrimeRegular(_)) #O(n*n)
	print("count: ", count)

def FindPrimesInRangeOptimal(n):
	#PrimeList=filter(lambda x: isPrimeOptimal(x), [ _ for _ in range(3,n)])
	#print(*PrimeList)
	count=0
	for _ in range(3,n):
		count+=isPrimeOptimal(_)[1]
		#print(_, isPrimeOptimal(_)) #O(n*n^0.5)
	print("count: ", count)

import cProfile
print("FindPrimesInRangeRegular(10001):-----")
cProfile.run("FindPrimesInRangeRegular(10001)")
print("FindPrimesInRangeOptimal(10001):---------")
cProfile.run("FindPrimesInRangeOptimal(10001)")
print("FindPrimesInRange(10001):---------")
cProfile.run("FindPrimesInRange(10001)")
print("FindPrimesInRangeV2(10001):---------")
cProfile.run("FindPrimesInRangeV2(10001)")

"""FindPrimesInRangeRegular(10001):-----
count:  5775223
         10003 function calls in 0.619 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.619    0.619 <string>:1(<module>)
     9998    0.617    0.000    0.617    0.000 PrimeNumbers.py:1(isPrimeRegular)
        1    0.002    0.002    0.619    0.619 PrimeNumbers.py:74(FindPrimesInRangeRegular)
        1    0.000    0.000    0.619    0.619 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


FindPrimesInRangeOptimal(10001):---------
count:  118755
         10003 function calls in 0.023 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.023    0.023 <string>:1(<module>)
     9998    0.021    0.000    0.021    0.000 PrimeNumbers.py:12(isPrimeOptimal)
        1    0.002    0.002    0.023    0.023 PrimeNumbers.py:84(FindPrimesInRangeOptimal)
        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


FindPrimesInRange(10001):---------
count:  44216798
         8777 function calls in 0.254 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.254    0.254 <string>:1(<module>)
        1    0.144    0.144    0.254    0.254 PrimeNumbers.py:25(FindPrimesInRange)
        1    0.000    0.000    0.000    0.000 PrimeNumbers.py:27(<listcomp>)
        1    0.000    0.000    0.254    0.254 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     8770    0.109    0.000    0.109    0.000 {method 'remove' of 'list' objects}


FindPrimesInRangeV2(10001):---------
count:  776630
         7 function calls in 0.140 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.140    0.140 <string>:1(<module>)
        1    0.139    0.139    0.140    0.140 PrimeNumbers.py:47(FindPrimesInRangeV2)
        1    0.000    0.000    0.000    0.000 PrimeNumbers.py:49(<listcomp>)
        1    0.000    0.000    0.140    0.140 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
