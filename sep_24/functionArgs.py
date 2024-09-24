
def calc(x=0, y=0, op="+"):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y

# x = input("Enter the first number: ")
# y = input("Enter the second number: ")
# op = input("Enter the operator (+, -, *, /): ")


# result = calc(int(x), int(y) , op)
#result = calc("+", 2, 3) # <-- This will not work

result = calc(op="-", y=5, x=3)
print(result)

result = calc(3, 4, op="*")
print(result)

# 2 + 3 - 5 / 2
