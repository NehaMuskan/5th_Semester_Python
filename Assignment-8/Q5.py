def fun(a,b):
    if b==0:
        return 0
    if a==0:
        return 1
    return b**a+fun(a-1,b)
   
a=int(input())
b=float(input())
print(fun(a-1,b))
#print(fun(a))