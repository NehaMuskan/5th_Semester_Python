def func(a):
    c=1
    for i in range(len(a)):
       if a[i]==" ":
           c=c+1
    return c
           
a=input()
print(func(a))