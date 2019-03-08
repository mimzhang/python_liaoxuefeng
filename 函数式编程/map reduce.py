from functools import reduce
## map的用法 ：
def f(x):
    return x*x
r = map(f,[1,2,3,4,5])
print(list(r))

print(list(map(str,[1,2,3,4,5])))

## reduce的用法：
# 把序列[1, 3, 5, 7, 9]变换成整数13579
def f1(x,y):
    return 10 * x + y
print(reduce(f1,[1,3,5,7,9]))
#把str转换为int
def char(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
print(reduce(f1,map(char,'13579')))