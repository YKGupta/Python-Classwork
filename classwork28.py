# Use of keyword arguments
def demo(*, name, age):
    print("Name is", name, "Age is", age)

demo(name = "Yash", age = 40)
demo(age = 40, name = "Yash")