class Singleton(type):
    def __init__(cls, name, bases, dict):
        super().__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class Base(): pass

class Derived(Base, metaclass=Singleton):
    pass

a1 = Derived()
a2 = Derived()

assert a1 == a2
