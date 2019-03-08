L1=sorted([3,-12,9], key=abs,reverse = True)
print(L1)

L2=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(L2)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(sorted(L,key=by_name))

def by_score(s):
    return -s[-1]
print(sorted(L,key=by_score))