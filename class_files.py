class administrator():
    pass

class master_admin(administrator):
    def __init__(self,name,passcode,password):
        self.name=str(name)
        self.passcode=int(passcode)
        self.password = password

class admin  (administrator):
    def __init__(self, name, passcode):
        self.name = str(name)
        self.passcode = int(passcode)


class customer ():
    def __init__(self, name, address, age):
        self.name = str(name)
        self.address= str(address)
        self.age= int(age)

    def __str__(self):
        return f"NAME:  {self.name} \nADDRESS: {self.address} \nAGE : {self.age}"

class computer ():
    def __init__(self,brand,model,ram,disk,price):
        self.brand = str(brand)
        self.model = str(model)
        self.ram = int(ram)
        self.disk = int(disk)
        self.price = int(price)

    def __str__(self):
        return f"BRAND:  {self.brand} \nModel: {self.model} \nRAM : {self.ram} \nDISK : {self.disk} \nPrice : {self.price}"

class orders (computer):
    def __init__(self,brand,model,ram,disk,price):
        self.brand = str(brand)
        self.model = str(model)
        self.ram = int(ram)
        self.disk=int(disk)
        self.price = int(price)