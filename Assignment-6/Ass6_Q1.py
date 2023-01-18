def func(s):
    strs=" "
    for i in s:
        if i in strs:
            strs+="*"
        else:
           strs+=i 
    return strs
       

s=input()
print(func(s))