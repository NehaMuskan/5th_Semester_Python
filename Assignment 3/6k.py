n=5
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(0,n):
    for j in range(i+2):
        print(" ",end="")
    for j in range(2 * (n-i-1) - 1):
        if j == 0 or j == 2 * (n-i-1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
   
    print()        
        