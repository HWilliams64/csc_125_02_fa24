def calc(op="+", *numbers):
    print(f"Args: {numbers}")
    if op == '+':
        total = 0
        for v in numbers:
            print(f"Adding {v}")
            total += v
        return total
    elif op == '-':
        total = 0
        for v in numbers:
            total -= v
        return total
    elif op == '*':
        total = 1
        for v in numbers:
            total *= v
        return total if len(numbers) > 0 else 0
    elif op == '/':
        if len(numbers) == 0:
            return 0
        
        total = numbers[0]
        for v in numbers[1:]:
            total /= v
        return total

r = calc('/', 5, 0)
print(r)