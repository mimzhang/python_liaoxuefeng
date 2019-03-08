#任何递归函数都存在<栈溢出>的问题
#n的阶乘
def fact0(n):
    if n==1:
        return 1
    return n*fact0(n-1)
print(fact0(1))  #fact0(1000)导致栈溢出

def fact(n): 
    def fact_iter(num,product):
        if num==1:
            return product
        return fact_iter(num-1,num*product)
    return fact_iter(n,1)
print(fact(5))