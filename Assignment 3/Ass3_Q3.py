def func(n):
    sum=1
    i=2
    while i*i<=n:
        if n%i==0:
            sum+=i+n/i 
        i+=1 
    if sum==n:
        return True
    return False
n=int(input())
print(func(n))