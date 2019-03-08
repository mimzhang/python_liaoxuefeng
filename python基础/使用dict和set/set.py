#set可以看成数学意义上的无序和无重复元素的集合
s = set([6,6,2,2,3,3])
print(s)     #结果为{2,3,6},表示s这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

s.add(4)
print(s) 

s.remove(4)
print(s)

#可以进行数学意义上集合的并交运算
s1 = set([1,2,3,4])
s2 = set([3,4,5,6])
print(s1 & s2)
print(s1 | s2)