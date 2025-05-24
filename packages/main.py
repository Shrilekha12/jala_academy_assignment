from package1 import BaseClass
from package2 import ChildClass
from package3 import OtherClass

print("Access from base class instance:")
base = BaseClass()
print(base._protected_field)
base._protected_method()

print("\nAccess from child class (different package):")
child = ChildClass()
child.access_protected()

print("\nAccess from unrelated class (different package):")
other = OtherClass()
other.access_protected()
