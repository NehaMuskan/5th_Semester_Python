
file1 = open('file1.txt', 'r')

#open file2 in writing mode
file2 = open('file2.txt','w')

#read from file1 and write to file2
for line in file1:
    file2.write(line)

#close file1 and file2
file1.close()
file2.close()

#open file2 in reading mode
file2 = open('file2.txt','r')

#print the file2 content
print(file2.read())

#close the file2
file2.close()