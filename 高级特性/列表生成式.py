#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,11)))
#生成[1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11)])
#筛选出仅偶数的平方:
print([x * x for x in range(1,11) if x%2 == 0])
#可以使用两层循环，可以生成全排列：
print([m + n for m in '123' for n in '456'])
#列出当前目录下的所有文件和目录名
import os
print(d for d in os.listdir('.'))# os.listdir可以列出文件和目录

#for循环其实可以同时使用两个甚至多个变量
d = {'x':'A','y':'B','z':'C'}
print(d.items())
for k,v in d.items():
    print(k,'=',v)

#列表生成式也可以使用两个变量来生成list
print([k+'='+v for k,v in d.items()])

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])