array=[16, 17, 4, 3, 5, 2]
print(*array)
Nmax=array[-1]
for x in range(len(array)-1,-1,-1):
	current=array[x]
	array[x] = Nmax

	if(current > Nmax):
		Nmax=current

"""
for x in range(len(array)-1):
	array[x]=array[x+1]
	for y in range(x+2, len(array)):
		if(array[x]<array[y]):
			array[x]=array[y]
"""
array[-1]=-1
print(*array)


3+4*N=>O(N)
3+4*N*N/2=>O(N^2)
log X

2^5=32
5=log 32 base 2
log x^N
Nlog x
log x base x=1
(2^_=2)

log 1024 b2=10
log 2^10 b2
10 log 2 b2

2^X=245325432
2^5=32
log => log X b2
---
Arithmatic
1+2+3...+n=n(n+1)/2 => O(n^2)
Harmonic Series
1+1/2+1/3+....+1/n=log n
----


n=?
n=32
log 256=>8
log 8 => 3
log n * log n

2^log n
2^8=256
a^logb base c
b^log a base c

256^log 2 b2


4
4! 4x3x2
log m*n=log m+log n
2+1+1.5



N! <> N^N
log n^n == nlogn<n^2
logn<n

10^2, 2^10

log 256*4=>10
log 256+ log 4=>10

for(i=0;i<n;i++)
	for(j=i;j<n;j++)
		print(*)
n*n
for(i=0;i<n;i++)
	for(j=0;j*j<n;j++)
		print(*)

n*sqrt(n)

for(i=0;i<n;i++)
	for(j=0;j<n;j*=2)//log n
		print(*)
n

n*logn
for(i=0;i<n;i*=2)
	for(j=0;j<n;j*=2)//log n
		print(*)

log^2 n

----
n
n,n/2,n/3.....n/n=n*(1+1/2....)
nlogn
logn=1+1/2+1/3+.....


nlogn>n

for
for 
for

1,2,3,2,55,8,3
2
for x in list
	for y in list after x
		if x==y
		 break

known_items
for x in list
	if x not in known_items
		push to known_items
	else:
		break
		
collection diction n^2
mydict = dict{}
for x in list
	mydict[x]+=1
	if mydict[x] > 1#O(1)
		break

sorting merge quick nlogn
n^2

