def brackets_balanced(s):
    brackets = {
        opening: closing for opening, closing in '() {} []'.split()
    }
    closing = set(brackets.values())
    stack = []
    for char in s:
        if char not in closing:
            if char in brackets:
                stack.append(brackets[char])
            continue
        try:
            expected = stack.pop()
        except IndexError:
            return False
        if char != expected:
            return False
    return not stack

def ensure_brackets_balanced(fn):
    for const in fn.__code__.co_consts:
        if not isinstance(const, str) or brackets_balanced(const):
            continue
        print(
            "WARNING - {.__name__} contains unbalanced brackets: {}".format(
                fn, const
            )
        )
    return fn

@ensure_brackets_balanced
def get_root_div_paragraphs(xml_element):
    return xml_element.xpath("//div[not(ancestor::div]/p")

