def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__
        for ind, val in enumerate(args):
            type_ = list(annotations.values())[ind]
            if not isinstance(val, type_):
                raise TypeError("Не верно введен тип аргумента")
        else:
            return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def chek_bool(a: int, b: bool) -> int:
    return a + b

@strict
def chek_str(a: str, b: str) -> str:
    return a + b

@strict
def chek_float(a: float, b: float) -> float:
    return a + b
