def inserts(l1,i=0):
    
    if(i==len(l1)):
        return l1;
    if(i%4==0):
        l1.insert(i,50)
    return inserts(l1,i+1)
    
l1=[1,2,3,4,5,6,7]
inserts(l1)
l1.remove(l1[0])
print(l1)