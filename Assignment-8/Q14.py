
def delete(l1,i=0):
    
    if(i==len(l1)):
        return l1;
    if(i%2==0 and i!=0):
        l1.remove(l1[i])
    return delete(l1,i+1)
    
l1=[1,2,3,4,5,6,7,8,9,10,11]
delete(l1)
print(l1)