def func(a):
    strs=""
    for i in a:
        strs=i+strs
    return strs
def ispalin(a):
    strs=func(a)
    if(len(a)!=len(strs)):
        return False
    if(a==strs):
        return True
    
           
a=input()
print(ispalin(a))