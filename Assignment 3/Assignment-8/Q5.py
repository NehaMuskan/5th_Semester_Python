def geo(n,r):
    if(n==0):
        return 0
    if(r==0):
        return 1
    return (r**n)+geo(n-1,r)
    
n=int(input())
r=float(input())
print(geo(n-1,r)+1)