def func(n):
   for i in range(1,n+1):
    
    # for space
    for j in range(1, n+1-i):
        print(' ', end='')
    
    # for decreasing pattern
    for j in range(i,0,-1):
        print(j, end='')
    
    # for increasing pattern 
    for j in range(2,i+1):
        print(j, end='')
    
    # Moving to next line
    print()
        
        
n=int(input())
func(n)
