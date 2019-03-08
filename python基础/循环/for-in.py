#打印list中的元素
names = ['aaa','bbb','ccc']
for name in names:
    print(name)

names = [111,222,333]
for name in names:
    print(name)

'''
#计算1-10的和
s = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in s:
    sum = sum + i
print(sum)
'''
print(list(range(5)))   #range(5)生成0-5的整数序列

#计算1-100的和
sum = 0
for i in range(101):   #注意是101
    sum = sum + i
print(sum)