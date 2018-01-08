STRATEGIES = []

def precondition(cond):
    def decorator(fn):
        fn.precondition_met = lambda **kwargs: eval(cond, kwargs)
        STRATEGIES.append(fn)
        return fn
    return decorator

@precondition("s.startswith('The year is ')")
def parse_year_from_declaration(s):
    return int(s[-4:])

@precondition("any(substr.isdigit() for substr in s.split())")
def parse_year_from_word(s):
    for substr in s.split():
        try:
            return int(substr)
        except Exception:
            continue

@precondition("'-' in s")
def parse_year_from_iso(s):
    from dateutil import parser
    return parser.parse(s).year

def parse_year(s):
    for strategy in STRATEGIES:
        if strategy.precondition_met(s=s):
            return strategy(s)

print(parse_year("The year is 2018"))
print(parse_year("2017-10-12"))
print(parse_year("In 2010 I was born"))

