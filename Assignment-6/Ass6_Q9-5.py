def func(a,n):
    strs=""
    for i in range(len(a)):
        if i!=n:
            strs=strs+a[i]
    return strs
            
    
a=input()
n=int(input())
print(func(a,n))