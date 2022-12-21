import math
def func(a,b):
    if(a==0):
        return 0
    if(b==0):
        return 0
    return a+func(a,b-1)
  
a=int(input())
b=int(input())
print(func(a,b))