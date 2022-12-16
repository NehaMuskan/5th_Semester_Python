def func(a,b):
    n=min(a,b)
    hcf=0
    for i in range(1,n+1):
        if(a%i==0) and (b%i==0):
            hcf=i 
    return hcf
        
a=int(input())
b=int(input())
print(func(a,b))