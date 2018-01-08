class FunctionHolder(object):
    def __init__(self, function):
        self.func = function
        self.called_count = 0
    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        finally:
            self.called_count += 1

def held(function):
    return FunctionHolder(function)

@held
def i_am_counted():
    pass

i_am_counted()
i_am_counted()
i_am_counted()
print(i_am_counted.called_count)

