from package1 import BaseClass

class OtherClass:
    def access_protected(self):
        obj = BaseClass()
        print("Accessing protected field from unrelated class:", obj._protected_field)
        obj._protected_method()
