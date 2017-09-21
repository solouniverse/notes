def ArrayPrintAllType(image):
	print("Print Array(AS IS):")
	M=N=range(len(image))
	for i in M:
		for j in N:
			print(image[i][j], end=" ")
		print()

	print("Print Array 2(Vertical):")
	M=N=range(len(image))
	for i in M:
		for j in N:
			print(image[j][i], end=" ")
		print()
		
	print("Print Array 3(Horizontal Flip):")
	M=N=len(image)
	for i in range(M):
		for j in range(N):
			print(image[i][N-1-j], end=" ")
		print()

	print("Print Array 4(Vertical Flip):")
	M=N=len(image)
	for i in range(M):
		for j in range(N):
			print(image[M-1-i][j], end=" ")
		print()

	print("Print Array 6(Rotate 90 & vertical flip):")
	M=N=len(image)
	for i in range(M):
		for j in range(N):
			print(image[M-1-j][N-1-i], end=" ")
		print()

	print("Print Array 7(Rotate 90):")
	M=N=len(image)
	for i in range(M):
		for j in range(N):
			print(image[M-1-j][i], end=" ")
		print()

	print("Print Array 5(Rotate 180):")
	M=N=len(image)
	for i in range(M):
		for j in range(N):
			print(image[M-1-i][N-1-j], end=" ")
		print()

	print("Print Array 8(Rotate 270):")
	M=N=len(image)
	for i in range(M):
		for j in range(N):
			print(image[j][N-1-i], end=" ")
		print()

M=3
image=[[x for x in range(y,y+M)] for y in [M*z for z in range(M)]]
ArrayPrintAllType()


"""
#print(image)
for x in image:
	for y in x:
		print(y, end=" ")
	print()
	
print("Print Array 7(Rotate 90):")
M=N=len(image)
for i in range(M):
	for j in range(N):
		print(image[M-1-j][i], end=" ")
	print()
exit()

dummyImage=[[0 for x in range(y,y+3)] for y in (0,4,7)]
#print("Print Array 7(Rotate 90):")
M=N=len(image)
for i in range(M):
	for j in range(N):
		#print(i,j,M-1-j,i)
		if(i<=M-1-j):
			image[i][j],image[M-1-j][i]=image[M-1-j][i],image[i][j]
print()
for x in image:
	for y in x:
		print(y, end=" ")
	print()
"""



"""
[[0, 1, 2], [4, 5, 6], [7, 8, 9]]
Print Array(AS IS):
0 1 2
4 5 6
7 8 9
Print Array 2(Vertical):
0 4 7
1 5 8
2 6 9
Print Array 3(Horizontal Flip):
2 1 0
6 5 4
9 8 7
Print Array 4(Vertical Flip):
7 8 9
4 5 6
0 1 2
Print Array 6(Rotate 90 & vertical flip):
9 6 2
8 5 1
7 4 0
Print Array 7(Rotate 90):
7 4 0
8 5 1
9 6 2
Print Array 5(Rotate 180):
9 8 7
6 5 4
2 1 0
Print Array 8(Rotate 270):
2 6 9
1 5 8
0 4 7
"""
