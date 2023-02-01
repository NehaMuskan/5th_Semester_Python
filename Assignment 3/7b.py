import math
def fun(x,n):
    sum=0
    for i in range(n,0,-1):
        sum=1+sum*x/i
    return sum   
x=int(input())
n=int(input())
print(fun(x,n))