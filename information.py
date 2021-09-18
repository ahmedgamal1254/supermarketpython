class Information:
    name,price,type='',0,''
    store={}
    def __init__(self,name,price,type):
        self.setName(name)
        self.setPrice(price)
        self.setType(type)

    def setName(self,name):
        if len(name.strip()) != 0:
            self.name=name
        else:
            print('you must write name of product')

    def getName(self):
        return self.name

    def setPrice(self,price):
        if price>0:
            self.price=price
        else:
            print('you must write price by postive number ')

    def getPrice(self):
        return self.price

    def setType(self,type):
        if len(type.strip()) != 0:
            self.type=type
        else:
            print('you must write type of product ')

    def getType(self):
        return self.type