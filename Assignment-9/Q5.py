file1=open("file1.txt","r")
file2=open("file2.txt","r")
file3=open("file3.txt","a")
i=0
str1=file1.read()
str2=file2.read()

s1=str1.split()
s2=str2.split()
for i in range(len(s1)):
    a=int(s1[i])
    b=int(s2[i])
    ans=b/a
    
    file3.write(str(ans)+" ")
file3.close()
file3=open("file3.txt","r")
print(file3.read())
file1.close()
file2.close()

