def func(a):
    word=a.split(" ")
    s=[]
    for i in word:
        s.insert(0, i)
 
 
    print(" ".join(s))
    
a=input()
func(a)