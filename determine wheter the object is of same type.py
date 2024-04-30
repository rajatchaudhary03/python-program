class MyClass:
    def _init_(self, name):
        self.name = name
# Function to determine if two objects have the same type, attributes, and memory address
def compare_objects(obj1, obj2):
    # Check if objects are of the same type
    type_same = type(obj1) == type(obj2)
    attrs_same = vars(obj1) == vars(obj2)
    same_object = obj1 is obj2
    return type_same, attrs_same, same_object
if _name_ == "_main_":
    obj1 = MyClass("John")
    obj2 = MyClass("John")
    obj3 = obj1
    print("Object 1:", obj1)
    print("Object 2:", obj2)
    print("Object 3:", obj3)
    type_same, attrs_same, same_object = compare_objects(obj1, obj2)
    print("\nAre obj1 and obj2 of the same type?", type_same)
    print("Do obj1 and obj2 have the same attributes?", attrs_same)
    print("Are obj1 and obj2 pointing to the same object?", same_object)
    type_same, attrs_same, same_object = compare_objects(obj1, obj3)
    print("\nAre obj1 and obj3 of the same type?", type_same)
    print("Do obj1 and obj3 have the same attributes?", attrs_same)
    print("Are obj1 and obj3 pointing to the same object?", same_object)


# use of filter function
def fun(n):
    if n%5 == 0:
        return True
    else:
        return False
lst1 = ['A','X','Y','3','M','4','D']
f1 = filter(str.isalpha,lst1)
print(list(f1))
lst2 = [5,18,10,6]
f2 = filter(fun,lst2)
print(list(f2))

# use of reduce() function
from functools import reduce
def getsum(x,y):
    return x+y
def getprod(x,y):
    return x*y
lst = [1,2,3,4,5]
s = reduce(getsum,lst)
p = reduce(getprod,lst)
print(s)
print(p)
