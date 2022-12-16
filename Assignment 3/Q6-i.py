def func(n):
    for i in range(0, n ):
       for j in range(0,i):
           print(" ",end="")
       for j in range(n-i,0,-1):
           print("*",end="")
       for j in range(n-i,1,-1):
           print("*",end="")
           
       print()
        
        
n=int(input())
func(n)