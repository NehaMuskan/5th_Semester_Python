class BankAccount:
    def acc(self,name,acc,savings):
        self.name=name
        self.acc=acc
        self.savings=savings
    def deposit(self,d):
        self.savings=self.savings+d
    def withdraw(self,w):
        self.savings=self.savings-w
    def display(self):
        print("NAME:",self.name)
        print("Account No.:",self.acc)
        print("Account Balance:",self.savings)
b1= BankAccount()
b1.acc("Divyam",199930062000,98000)
ch=''
while(ch!=5):
    print("MAIN MENU")
    print("1.DEPOSIT")
    print("2.WITHDRAW")
    print("3.BALANCE EQUERY")
    print("4.EXIT")
    ch=int(input())
    if ch==1:
        d=int(input())
        b1.deposit(d)
    if ch==2:
        w=int(input())
        b1.withdraw(w)
    if ch==3:
        b1.display()
    if ch==4:
       break
        