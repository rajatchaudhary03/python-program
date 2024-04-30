def compare_objects(obj1, obj2):
    type_check = type(obj1) == type(obj2)
    situation_type_check = isinstance(obj1, type(obj2)) or isinstance(obj2, type(obj1))
    attributes_check = obj1.__dict__ == obj2.__dict__
    same_object_check = obj1 is obj2
