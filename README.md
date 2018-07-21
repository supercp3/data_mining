# data_mining
it will be a great book for data mining
编辑距离：
常用来判断两个字符串的相似程度：
string1到string2的编辑距离计算三种方式：
1 插入
2 删除
3 替换
经过插入、删除和替换三种方式从word1装换到word2的最小次数n,
然后editdistance=1-n/max(len(str1),len(str2))
通常使用动态规划来进行计算，递推公式为：
matrix[i][j]=matrix[i-1][j-1]   if word[i]=word[j]
            =min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+1) else

