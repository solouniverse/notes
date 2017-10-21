MAX=6
#Array=[[x for x in range (y)] for y in [z*3 for z in range (MAX)]]
Array=[[x for x in range (y, y+MAX)] for y in range (0,MAX*MAX,MAX)]
#print(Array)

def PrintArray(Array):
	for x in range(MAX):
		for y in range(MAX):
			print("%3d" %Array[x][y], end=" ")
		print()
	print()
PrintArray(Array)

for j in range(MAX//2):
	for i in range(j,MAX-j-1):
		temp=Array[j][i]
		Array[j][i]=Array[MAX-1-i][j]
		Array[MAX-1-i][j]=Array[MAX-j-1][MAX-j-1-i]
		Array[MAX-j-1][MAX-j-1-i]=Array[i][MAX-j-1]
		Array[i][MAX-j-1]=temp
		print("%d-%d:--------------------------------------------"%(j,i))
		PrintArray(Array)
	
exit()

for j in range(MAX-1):
	#for i in range(j,(MAX-j)//2):
	for i in range(j,MAX-j-1):
		Array[j][i],Array[i][MAX-1-j]=Array[i][MAX-1-j],Array[j][i]
		Array[j][i],Array[MAX-1-j][MAX-1-i-j]=Array[MAX-1-j][MAX-1-i-j],Array[j][i]
		Array[j][i],Array[MAX-1-i-j][j]=Array[MAX-1-i-j][j],Array[j][i]

PrintArray(Array)
exit()
Array[0][0],Array[0][MAX-1]=Array[0][MAX-1],Array[0][0]
Array[0][0],Array[MAX-1][MAX-1]=Array[MAX-1][MAX-1],Array[0][0]
Array[0][0],Array[MAX-1][0]=Array[MAX-1][0],Array[0][0]

Array[0][1],Array[1][MAX-1]=Array[1][MAX-1],Array[0][1]
Array[0][1],Array[MAX-1][MAX-1-1]=Array[MAX-1][MAX-1-1],Array[0][1]
Array[0][1],Array[MAX-1-1][0]=Array[MAX-1-1][0],Array[0][1]


