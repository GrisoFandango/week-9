class CashRegister :
# Comment 1: Initialize the objects and sets itemCount and totalPrice at 0
    def __init__(self) : 
        self._itemCount = 0 
        self._totalPrice = 0.0
        self._totalSale = 0
# Comment 2: It is a function that keep count when we add an item and
# increase the totalPrice of that item.
    def addItem(self, price) :
        self._itemCount = self._itemCount + 1 
        self._totalPrice = self._totalPrice + price
# Comment 3: It is a function that can be used to print the output of the totalPrice
    def getTotal(self) :
        return self._totalPrice 
# Comment 4: It is a function that can be used to print the output of the itemCount
    def getCount(self) :
        return self._itemCount 
# Comment 5: This function allow to reset the value of itemCount and totalPrice to 0
    def clear(self) :
        self._itemCount = 0
        self._totalPrice = 0.0
    def getPounds (self):
        self._totalSale = ("%.0f"%self._totalPrice)
    def giveChange(self,payment):
        self._change = (payment - self._totalPrice)
'''
request = input ("do you want add item? Y/N")

while request== "Y" or request == "y":
    registerx = CashRegister()
    registerx.addItem(float(input("What is the price?: ")))
    request = input ("do you want add item? Y/N")

'''
registerx = CashRegister()   
def adding():
    
    #registerx = CashRegister()
    registerx.addItem(float(input("What is the price?: ")))
    
#registerx.addItem(float(input("What is the price?: ")))
#registerx.addItem(float(input("What is the price?: ")))
#registerx.addItem(float(input("What is the price?: ")))
    
request = input ("do you want add item? Y/N")

while request== "Y" or request == "y":
    adding()
    request = input ("do you want add item? Y/N")

registerx.getPounds()
registerx.giveChange(float(input("Amount money received to pay register1?")))
print("registerx_itemCount is: \t", registerx._itemCount)
print("registerx_totalPrice is: \t", registerx._totalPrice)
print("registerx_totalSale is: \t", registerx._totalSale)
print("registerx_giveChange is: \t",registerx._change,"\n")
'''


register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
register1.getPounds()
register1.giveChange(float(input("Amount money received to pay register1?")))

register2 = CashRegister()
register2.addItem(1.90)
register2.addItem(2.30)
register2.getPounds()
register2.giveChange(float(input("Amount money received to pay register2?")))

print("register1_itemCount is: \t", register1._itemCount)
print("register1_totalPrice is: \t", register1._totalPrice)
print("register1_totalSale is: \t", register1._totalSale)
print("register1_giveChange is: \t",register1._change,"\n")

print("register2_itemCount is: \t", register2._itemCount)
print("register2_totalPrice is: \t", register2._totalPrice)
print("register2_totalSale is: \t",register2._totalSale)
print("register2_giveChange is: \t",register2._change)

'''








