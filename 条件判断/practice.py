# -*- coding: utf-8 -*-
h = 1.75
w = 80.5
bmi = w / (h * h)     #BMI要小写，大写表示常量
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')