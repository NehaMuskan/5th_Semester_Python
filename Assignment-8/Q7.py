def subsetSum(arr, l, r,sum=0):
    if(l>r):
        print(sum,end=" ")
        return
    subsetSum(arr,l+1,r,sum+arr[l])
    subsetSum(arr,l+1,r,sum)
arr=[5,4,3]
n=len(arr)
subsetSum(arr,0,n-1)