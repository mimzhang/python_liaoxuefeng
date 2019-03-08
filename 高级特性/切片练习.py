# 利用切片操作，实现一个trim()函数，
# 去除字符串首尾的空格，
# 注意不要调用str的strip()方法。

# -*- coding: utf-8 -*-
'''
#递归
def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    if s[-1:] == ' ':
        return trim(s[:-1])
    return s
'''
def trim(s):
    i=0
    while i < len(s):
        if s[i] == ' ':
            i = i + 1
        else:
            break
    start = i            
    
    i=len(s)            
    while i > 0:
        if s[i-1] == ' ':
            i = i - 1
        else:
            break
    end = i
    return s[start:end]
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')