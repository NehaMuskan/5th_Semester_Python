
file1 = open('file1.txt', 'r')
v=0
w=0
str=file1.read()
for i in str:
    if(i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='o' or i=='O' or i=='u' or i=='U'):
        v=v+1
w=len(str.split())
print(v)
print(w)
file1.close()