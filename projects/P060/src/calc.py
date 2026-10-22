import math

def total(values):
    numbers = list(values)
    for value in numbers:
        if type(value) not in (int, float):
            raise TypeError("numeric only")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("finite numbers only")
    result = sum(numbers)
    if isinstance(result, float) and not math.isfinite(result):
        raise ValueError("non finite result")
    return result
