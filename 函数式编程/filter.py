## filter(),一个“筛选”函数
# 只保留奇数
def is_odd(a):
    return a%2 == 1
L = list(filter(is_odd,[1,2,5,6,8,9]))
print(L)


## filter()筛选出回数,例如12321，909
def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')