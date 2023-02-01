def fun(a,b):
    if(a==0 or b==0):
        return 0
    if(a==b):
        return a
    if(a > b):
        return fun(a-b,b)
    else:
        return fun(a,b-a)
   
a=int(input())
b=int(input())
if(fun(a,b)==1):
    print("True")
else:
    print("False")