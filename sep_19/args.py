z = 10

def add(x, y):
    # global z <- DO NOT DO
    z = x + y
    return z

r = add(3, 5)
print("r =", r)
print("z =", z)