class Details:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def sayHemlo(self):
        print("Hemlo", self.name)

ob1 = Details("Yash", 18)
ob2 = Details("Kumar", 18)
ob1.sayHemlo()
ob2.sayHemlo()