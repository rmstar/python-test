#!/usr/bin/env python3

class A():
    def __init__(self, *args, **kwargs):
        print("A::args", args, " kwargs", kwargs)

class Factory():
    def register(self, methodname, cls, *args, **kwargs):
        setattr(self, methodname, Functor(cls, *args, **kwargs))
    def unregister(self, methodname):
        delattr(self, methodname)

class Functor():
    def __init__(self, cls, *args, **kwargs):
        self._cls = cls
        self._args = list(args)
        self._kwargs = kwargs
    def __call__(self, *args, **kwargs):
        self._args.extend(args)
        self._kwargs.update(kwargs)
        return self._cls(*self._args, **self._kwargs)


f = Factory()
f.register('createA', A, 1, 2, foo = 1)
a = f.createA(3, bar = 20)

