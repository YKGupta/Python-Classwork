# More on keyword and positional arguments
def demo(x, y, *, name, age, clas = 10, state, city = "Kanpur", blood):
    print(x*y, name, age, clas, state, city, blood)

demo(4, 7, name = "Yash", age = 40, clas = 12, state = "UP", city = "Kanpur", blood = "O+")
demo(12, 2, state = "UP", blood = "O+", name = "Yash", age = 40)