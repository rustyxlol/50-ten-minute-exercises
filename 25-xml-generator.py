def myxml(tagname, content='', **kwargs):
    attrs = ''
    for key, value in kwargs.items():
        attrs = attrs + f' {key}="{value}"'
    return f'<{tagname}{attrs}>{content}</{tagname}>'


def factorial(*args):
    result = 1
    if args:
        for arg in args:
            result *= arg
    return result


if __name__ == "__main__":
    print(myxml('tagname', 'hello', a=1, b=2, c=3))
    print(factorial(1, 2, 3, 4))
