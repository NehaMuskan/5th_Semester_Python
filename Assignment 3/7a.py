import math
def fun(x,n):
    sum=1
    term=1
    y=2
    for i in range(1,n):
        term=term*(-1)
        m=term*math.pow(x,y)/fact(y)
        sum=sum+m
        y=y+2
    return sum   
def fact(n):
    if n==0:
        return 0
    if n==1:
        return 1 
    if n==2:
        return 2
    return n*fact(n-1)
x=int(input())
n=int(input())
print(fun(x,n))