def func(a,b):
    if(len(a)!=len(b)):
        return False
    m={}
    for i in range(len(a)):
        if a[i] in m:
            m[a[i]]+=1 
        else:
            m[a[i]]=1
    for i in range(len(b)):
        if b[i] in m:
            m[b[i]]-=1 
        else:
            return False
    keys=m.keys()
    for i in keys:
        if (m[i]!=0):
            return False
    return True
           
a=input()
b=input()
print(func(a,b))