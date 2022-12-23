class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def purchase(self,item):
        if(item>self.quantity):
            print("Insufficent quantity")
        else:
            self.quantity-=item
    def addstock(self,a):
        self.quantity+=a
    def display(self):
        print("NAME:",self.name)
        print("PRICE:",self.price)
        print("QUANTITY:",self.quantity)
b1= Item("Divyam",500,100)
b1.display()
b1.purchase(20)
b1.addstock(10)
print("-------------")
b1.display()

