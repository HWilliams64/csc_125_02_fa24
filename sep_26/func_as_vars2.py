from typing import Callable, Union
from csc_125_02_fa24.sep_26.func_as_vars import add


def calc(
    f: Callable,
    x: Union[int, float],
    y: Union[int, float]
) -> Union[int, float]:
    return f(x, y)


r = calc(add, 2, 3.0)
print(f"The output = {r}, datatype = {type(r).__name__}")
