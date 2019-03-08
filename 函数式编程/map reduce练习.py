# 利用map()函数，
# 把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
# -*- coding: utf-8 -*-
def normalize(name):
    name = name.lower()
    name = name[0].upper() + name[1:]
    return name
    # return name.capitalize()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

## 编写一个prod()函数，
# 可以接受一个list并利用reduce()求积
from functools import reduce
def f(x,y):
        return x*y
def prod(L):
    return reduce(f,L)
# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!') 