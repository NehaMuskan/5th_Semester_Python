def printthearray(arr,n):
    for i in range(0, n):
        print(arr[i], end = " ")
     
    print()
def func(n,arr,i):
    if(i==n):
        printthearray(arr,n)
        return
    arr[i]=0
    func(n,arr,i+1)
    arr[i]=1 
    func(n,arr,i+1)
n=4
arr=[None]*n 
func(n,arr,0)