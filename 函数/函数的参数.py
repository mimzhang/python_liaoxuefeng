## 默认参数
# #须必选参数在前，默认参数在后
def power(x, n=2): #把第二个参数n的默认值设定为2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,3))
# 默认参数必须指向不变对象！
'''
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())   #输出['END']
print(add_end())   #输出['END', 'END']
'''
def add_end(L=None):
    if L == None:
        L = []
    L.append('END')
    return L
print(add_end())   #输出['END']
print(add_end())   #输出['END']

## 可变参数,加*变为可变参数
def calc(*numbers):  #计算a^2 + b^2 + c^2 + ……
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2))
#如果已经有一个list或者tuple，要调用一个可变参数
nums = [1,2,3,4]
print(calc(*nums))

## 关键字参数，**某某
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('bob',35,city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

## 命名关键字参数，限制关键字参数的名字
def person1(name, age, *, city, job):
    print(name, age, city, job)
#person1('Jack', 24,city='Beijing', job='Engineer',gender='M')
#报错，gender='M'

## 参数组合
#顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
#通过一个tuple和dict，也可以调用上述函数
print('\n')
args = (1, 2, 3, 4)  #定义tuple
kw = {'d': 99, 'x': '#'}  #定义dict
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)