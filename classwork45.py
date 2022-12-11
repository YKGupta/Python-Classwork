class Details:
    def __init__(self, na, ag, gen):
        self.name = na
        self.age = ag
        self.gender = gen

ob1 = Details("Yash", 18, "Male")
ob2 = Details("Kumar", 18, "Male")
print(ob1.name, ob1.age, ob1.gender)
print(ob2.name, ob2.age, ob2.gender)