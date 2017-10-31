Prime factors upto given number.
def isPrime(n):
#O(n)
	for i in range(n):#Check for factors upto n-1
		if(n%i==0):
			return False
	else:
		return True

def isPrime_sqrt(n):
#O(sqrt(n))
	for i in range(n):
		if(n%i==0):
			return False
		if(i*i >=n): #Check for factors upto sqrt(n) only
			return True

def PrimeFactors_1(n):
#O(n*n*n)
	factorsList=[]
	for x in range(n):
		for y in range(n-1): #Check for factors upto n-1
			if(x*y==n):
				if(isPrime(x)):
					factorsList.append(x)
				if(isPrime(y)):
					factorsList.append(y)
	return factorsList
	
def PrimeFactors_2(n):
#O(n*n*sqrt(n))
	factorsList=[]
	for x in range(n):
		for y in range(n-1):
			if(x*y==n):
				if(isPrime_sqrt(x)):
					factorsList.append(x)
				if(isPrime_sqrt(y)):
					factorsList.append(y)

	return factorsList

def getPrimeNumbersUptoN(n):
#O(n*sqrt(n))
	PrimeNumbersUptoN=[]
	for y in range(2,n):
		if(isPrime_sqrt(y)):
			PrimeNumbersUptoN.append(y)
	return(PrimeNumbersUptoN)

def getPrimeNumbersUptoN_2(n):
#O(n*pi(sqrt(n)))
	PrimeNumbersUptoN=[2]
	for x in range(3,n):
		for y in PrimeNumbersUptoN:
			if(x%y==0):
				break
			if(y*y>=x):
				PrimeNumbersUptoN.append(x)
		else:		
			PrimeNumbersUptoN.append(x)
	return(PrimeNumbersUptoN)

def PrimeFactors_3(n):
#O(pi(n)*pi(n))
	factorsList=[]
	PrimeNumbersUptoN=getPrimeNumbersUptoN(n)	
	for x in PrimeNumbersUptoN:
		for y in PrimeNumbersUptoN:
			if(x*y==n):
				factorsList.append(x)

	return factorsList

def PrimeFactors_4(n):
#O(pi(sqrt(n))*pi(n))
	factorsList=[]
	PrimeNumbersUptoN=getPrimeNumbersUptoN_2(n)	
	for x in PrimeNumbersUptoN:
		for y in PrimeNumbersUptoN:
			if(x*y==n):
				factorsList.append(x)
		if(x*x>=n):
			break
				

	return factorsList
	


