def div1(x, y):
    return x / y

def div2(x, y):
    return div1(x, y)

def div3(x, y):
    return div2(x, y)

def div4(x, y):
    return div3(x, y)

def div5(x, y):
    return div4(x, y)

r = div5(1, 0) # r = 1 / 0

print(r)