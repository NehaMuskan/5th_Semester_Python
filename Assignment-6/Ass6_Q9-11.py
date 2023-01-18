def freq(l1):
    l2={}
    for i in l1:
       if i in l2:
           l2[i]+=1
       else:
           l2[i]=1 
    ans=max(l2,key=l2.get)
    return ans
        
   
           
l1=input("Enter:")
print(freq(l1))