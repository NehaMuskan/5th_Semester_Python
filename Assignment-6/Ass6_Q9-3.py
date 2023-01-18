def func(a):
    str1=""
    str2=""
    if(len(a)%2!=0):
        return False
    half=len(a)//2 
    for i in range(0,half):
        str1=""+a[i]
    for half in range(half,len(a)):
        str2=""+a[half]
    if(str1==str2):
        return True
    return  False
    
    
a=input()
print(func(a))