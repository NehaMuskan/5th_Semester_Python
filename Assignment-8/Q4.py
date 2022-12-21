def har(a):
    if(a==0):
        return 0
    return (1/a)+har(a-1)
    
a=int(input())
print(har(a))