from package1 import BaseClass

class ChildClass(BaseClass):
    def access_protected(self):
        print("Accessing protected field from child:", self._protected_field)
        self._protected_method()
