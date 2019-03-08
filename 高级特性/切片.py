## 创建一个0-99的数列
L = list(range(100))
print(L)

#list的切片操作：
print(L[:10])#切片取出前10个数
print(L[10:20])#前11-20个数
#倒数切片
print(L[-1:])# 结果[99]
print(L[-10:])#切片取出后10个数
print(L[-10:-5]) #[90, 91, 92, 93, 94]
#每*个取一个
print(L[:10:2])#前10个数，每两个取一个
print(L[::5])#所有数，每5个取一个
#print(L[:])#原样复制一个list

# 字符串'xxx'也可看作一种list，每个元素就是一个字符
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

# tuple也可以用切片操作
print((0, 1, 2, 3, 4, 5)[:3])#(0, 1, 2)
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])