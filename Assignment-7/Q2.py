def sumList(l1):
    l2=[]
    sum=0
    for i in l1:
        sum+=i 
        l2.append(sum)
    return l2
l1=[2,4,3,2,4,6,7,2]
print(sumList(l1))