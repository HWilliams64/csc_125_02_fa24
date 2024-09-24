def simple(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    print(kwargs["a"], args[0])

simple(1, 2, 3, a=4, b=5, c=6)