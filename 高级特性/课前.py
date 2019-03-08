#构造一个1, 3, 5, 7, ..., 99的列表
L=[]
i=1
while i <= 99:
    L.append(i)
    i=i+2
print(L)
# 取L中的一半元素
n=0
L1=[]
while n < (len(L)/2):
    # L1[n]=L[n]     #错误，空数组L1不能直接指定位置L1.append(1)
    L1.append(L[n])  
    n=n+1
print(L1)