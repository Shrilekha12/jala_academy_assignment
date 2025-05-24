class Class1:
    def __init__(self):
        print("Class1 constructor called")

    def greet(self):
        print("Hello from Class1!")
class Class2:
    def __init__(self):
        print("Class2 constructor called")

    def greet(self):
        print("Hello from Class2!")
from .class1 import Class1
from .class2 import Class2
from mypackage import Class1, Class2

def main():
    obj1 = Class1()
    obj1.greet()

    obj2 = Class2()
    obj2.greet()

if __name__ == "__main__":
    main()
