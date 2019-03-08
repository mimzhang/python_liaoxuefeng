#tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
a1 = (1,2,3)   #不可变元组
a2 = (1,[2,3]) #可变元组
d1 = {1:a1}
print(d1)
d2 = {1:a2}   #未报错，dict的value可以为可变元组
print(d2)
d3 = {a1:1}
print(d3)     #d1,d2,d3均未报错

'''
d4 = {a2:2}   #报错，可变元组不可作为dict的key
print(d4)
'''

s1 = set(a1)
print(s1)

s2 = set(a2)  #报错，不可将可变元组传入set中
print(s2)