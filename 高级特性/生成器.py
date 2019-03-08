# 生成器：generator,其保存的是算法
g = (x * x for x in range(3))
# 打印出generator的元素
for n in g:
    print(n)

## 定义generator的另一种方法，yield
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b   #把print(b)改为yield b
        a , b = b , a+b  #a=b;b=a+b
        n = n+1
    return 'done'
print(fib(5))

## 定义一个generator，依次返回数字1，3，5
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5