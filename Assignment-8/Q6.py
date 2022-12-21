def func(n):
    if(n==0):
        return 0
    n+=func(n-2)
    return n
    
n=int(input())
print(func(n-2)+n)