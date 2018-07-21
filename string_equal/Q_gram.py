
def partition(stringlist,q):
	stringNew=stringlist.replace(" ","")
	length=len(stringNew)
	listRes=[]
	for i in range(0,length):
		str=""
		if i+q<length or i+q==length:
			for j in range(i,i+q):
				str+=stringNew[j]
			listRes.append(str)
	return listRes

def Q_gram(str1,str2,q):
	str1_list=partition(str1,q)
	str2_list=partition(str2,q)
	num=0
	for i in str1_list:
		for j in str2_list:
			if i==j:
				num=num+1
	res=num/max(len(str1_list),len(str2_list))
	return res



str1="yuanchao"
str2="yuanchao2"
res=Q_gram(str1,str2,2)
print(res)