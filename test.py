def named(**kwargs):
    print(kwargs)


details = {"name": "Ali", "age": 25}

named(**details)


def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


nums = (1, 2, 3, 4, 5)
print(multiply(*nums))
