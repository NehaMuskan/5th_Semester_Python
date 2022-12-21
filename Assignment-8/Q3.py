def pow(a,b):
    if(b==0):
        return 1
    return a*pow(a,b-1)
    
a=int(input())
b=int(input())
print(pow(a,b))