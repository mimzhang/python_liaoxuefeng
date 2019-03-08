# -*- coding: utf-8 -*-
# 汉诺塔的移动，请编写move(n, a, b, c)函数
# 它接收参数n
# 表示3个柱子A、B、C中第1个柱子A的盘子数量
# 请打印出把所有盘子从A借助B移动到C的方法
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)    #把 n - 1 个盘子 从a 借助 c 移动到 b
        print(a, '-->', c)      # 把 a 中最后一个盘子移动到 c
        move(n-1, b, a, c)      # 把 n - 1 个盘子 从 b 借助 a 移动到 c  
move(4,1,2,3)
