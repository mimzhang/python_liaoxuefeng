# -*- coding:utf-8 -*-
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0的两个解。
import math

def quadratic(a,b,c):
    derta = b*b-4*a*c
    if a == 0:
        print('a不可为0')
    elif derta >= 0:
        x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
        return x1,x2
    else:
        print('不是一元二次方程')
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
quadratic(0, 3, -4)
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')