# 通过key计算位置的算法称为哈希算法（Hash）。
# dict的key必须是不可变对象。  str、int为不可变对象，list为可变对象
# dict内部存放的顺序和key放入的顺序是没有关系的。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67  #把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
print(d)

d['Adam'] = 999  #一个key只对应一个value，多次对一个key放入value，后面的值会把前面的冲掉
print(d)

d.pop('Michael')
print(d)


#str不可变
a = 'abc'
b = a.replace('a', 'A')
print(b)   #结果为Abc
print(a)   #结果为abc


