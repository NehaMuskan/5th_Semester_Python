class Student:
    def __init__(self,roll,name,marklist,perc,grade,divi,stream):
        self.roll=roll
        self.name=name
        self.marklist=marklist
        self.perc=perc
        self.grade=grade
        self.divi=divi
        self.stream=stream
    def getMarks(self):
        print("Enter marks of subject : ")
        for i in range(0, 5):
            self.marklist.append(int(input()))
        
    def getStream(self,s):
        if s=='A':
            self.stream="Arts"
        elif s=='C':
            self.stream="Commerce"
        elif s=='S':
            self.stream="Science"
        else:
            print("Invalid input")
    
    def percentage(self):
        #print(self.marklist)
        self.perc=sum(self.marklist)/len(self.marklist)
    def gradegen(self):
        if self.perc>=90:
            self.grade='A'
        elif self.perc>=80:
            self.grade='B'
        elif self.perc>=65:
            self.grade='C'
        elif self.perc>=40:
            self.grade='D'
        else:
            self.grade='E'
    def display(self):
       print("Roll no.:",self.roll)
       print("Name:",self.name)
       print("Marklist:",)
       print("Grade:",self.grade)
       print("percentage:",self.perc)
       print("Division:",self.divi)
       print("Stream:",self.stream)
 
 
s= Student(3251,"Divyam",[],0,"E","1st","C")
s.getStream(input("Enter stream:"))
s.getMarks()
s.percentage()
s.gradegen()
s.display()
 
        
