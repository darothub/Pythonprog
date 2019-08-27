class Me:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def walk(self):
        print("I walk and conquer")
    
    def nomen(self):
        print(f"I am {self.name} of {self.height} height")
    


darot = Me('Darot', 5.5)


darot.walk()
darot.nomen()
        
class Family:
    house = "Lagos"
    def __init__(self, name):
        self.surname = "Eze"
        self.name = name
    
    def introduce(self):
        print(f"I am {self.surname} {self.name}")

    @staticmethod
    def anonymous():
        print("This is a static method")
    
    @classmethod
    def house_add(cls):
        print (cls.house)


chidiogo = Family("Chidiogo")

chidiogo.introduce()
Family.anonymous()
Family.house_add()


print(int.__add__(5, 8))

sum = [x<<1 for x in range(10)]

print(sum)