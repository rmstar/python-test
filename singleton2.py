def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class A():
    pass

@singleton
class B():
    pass

a1 = A()
a2 = A()
b = B()
assert a1 == a2
assert b != a1
