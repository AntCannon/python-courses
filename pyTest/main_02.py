def add(a: int | float, b: int | float) -> int | float:
    return a + b


def divide(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise ValueError("Cannot divide by zer0")

    return a / b
