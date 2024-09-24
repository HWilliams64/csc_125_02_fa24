def calc(x: float, y: float, op="+") -> float:
    """
    This is a function at preforms a calculation on 2 numbers based on the
    operation and returns the result.
    """

    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return 0

print(calc(5, 3, '+')) 
