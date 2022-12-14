# Inheritance
class People:
    name = "Demo"
    age = 20

    def sayHemlo(self):
        print("Hemlo")

class Worker(People):
    salary = 100
    
    def sayBye(self):
        print("Bye")

ob = Worker()
print(ob.name, ob.age, ob.salary)
ob.sayBye()
ob.sayHemlo()