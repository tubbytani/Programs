class hello:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=hello("hi",24)
print(p.__init__("hi",45))
#output is None
class fruit:
    def __init__(self,name1,name2,name3):
        self.name1=name1
        self.name2=name2
        self.name3=name3
    def print1(self):
            print("sweet "+self.name1+" is ready")
    def print2(self):
            print("sweet "+self.name2+" is ready")
    def print3(self):
            print("sweet "+self.name3+" is ready")

    '''   
    def print1(self,name1):
            print("sweet "+self.name1+" is ready")
    def print2(self,name2):
            print("sour "+self.name2+" is ready")
    def print3(self,name3):
            print("red "+self.name3+" is ready")    
    '''        
p=fruit("papaya","jam","salad")
print(p.print1()) #remove print()
print(p.print2())
print(p.print3())
