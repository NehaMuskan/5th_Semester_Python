
file2 = open('file2.txt', 'w')
s1=input()
while s1!="":
    file2.write(s1.capitalize())
    s1=input("\nEnter:")
file2.close()
file2=open("file2.txt","r")
print(file2.read())