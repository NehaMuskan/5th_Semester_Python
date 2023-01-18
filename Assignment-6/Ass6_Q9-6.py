vowels = ['a', 'e', 'i', 'o', 'u']
def func(a):
   cv=0
   cc=0
   for i in a:
       if i in vowels:
           cv=cv+1;
       else:
           cc+=1 
   print("count vowel:",cv) 
   print("count consonants:",cc) 
            
    
a=input()
func(a)