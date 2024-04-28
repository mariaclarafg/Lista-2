def compose(func1, func2):
    def composed_function(*x1, **x2):
        return func1(func2(*x1, **x2))
    return composed_function


def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

composed = compose(add_one, multiply_by_two)
result = composed(3)
print("Composed function:", result)