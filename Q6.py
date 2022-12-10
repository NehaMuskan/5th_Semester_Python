def list1(n):
    l2=[]
    for i in range(1,6):
        l2.append(n*i)
    return l2
n=int(input())
print(list1(n))