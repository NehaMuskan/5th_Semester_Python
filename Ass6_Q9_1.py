def func(a):
    strs=""
    for i in a:
        strs=i+strs
    return strs
           
a=input()
print(func(a))