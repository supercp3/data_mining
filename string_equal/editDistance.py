import numpy as np

def edit(str1,str2):
	m=len(str1)
	n=len(str2)
	lenmax=max(m,n)
	matrix=np.zeros(shape=(m,n))
	#print("原始矩阵")
	#print(matrix)
	for i in range(1,m):
		matrix[i][0]=matrix[i-1][0]+1
	for i in range(1,n):
		matrix[0][i]=matrix[0][i-1]+1
	#print("初始化矩阵")
	#print(matrix)
	temp=0
	for i in range(1,m):
		for j in range(1,n):
			if str1[i]==str2[j]:
				temp=0
			else:
				temp=1
			matrix[i][j]=min(matrix[i-1,j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+temp)
	#print("最终的矩阵")
	#print(matrix)
	#print(matrix[m-1][n-1])
	number=matrix[m-1][n-1]
	res=1-number/lenmax
	return res



str1="yuanhao"
str2="yuanchao2"
result=edit(str1,str2)
print("编辑距离为：")
print(result)