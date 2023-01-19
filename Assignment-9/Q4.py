file1=open("file1.txt","w")
file1.write("HI SHIVANM\nMy name is Neha")
file1.close()
try:
    file1=open("file1.txt","r")
    file2=open("file2.txt","w")
except IOError:
    print("File doesn't exist")
cont=file1.readlines()
type(cont)
for i in range(0,len(cont)):
    if(i%2!=0):
        file2.write(cont[i])
    else:
        pass
file2.close()
file2=open("file2.txt","r")
print(file2.read())
    
    

