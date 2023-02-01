def fun(n):
    sum=0
    val=n
    while n>0:
        r=n%10
        sum=sum+(r*r*r)
        n=n//10
        
    if(sum==val):
        return True
    else:
        return False
   
#x=int(input())
n=int(input())
print(fun(n))