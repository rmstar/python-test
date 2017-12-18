class Shape:
    def __init__(self, *, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self, *, color, **kwds):
        self.color = color
        super().__init__(**kwds)

cs = ColoredShape(shapename='circle', color='red')
print(cs.color)
print(cs.shapename)

