def noduplicates(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    for i in l2:
        print(i, end =" ")
l1=[2,4,3,2,4,6,7,2]
noduplicates(l1)