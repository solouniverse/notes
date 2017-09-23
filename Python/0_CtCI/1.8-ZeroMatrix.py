def ArrayPrint(array):
	for i in range(M):
		for j in range(M):
			print(array[i][j], end = " ")
		print()
	print()
M=4
#Array=[[y for y in range(x,x+M)] for x in [z*M for z in range(M)]] 
Array= [[0, 1, 2, 3], [0, 0, 6, 7], [8, 9, 0, 11], [12, 13, 14, 15]]
ArrayPrint(Array)
iList=[]
jList=[]

for i in range(M):
	for j in range(M):
		if 0 == Array[i][j]:
			iList.append(i)
			jList.append(j)

for i in range(M):
	for j in range(M):
		if(i in set(iList) or j in set(jList)):
			Array[i][j]=0

ArrayPrint(Array)
