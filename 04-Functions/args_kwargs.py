def fun(a, b, c, d, *args, **kwargs):
    print(args)
    print(kwargs)
    print(a, b, c, d)
    return a + b


print(fun(3, 7, 8, 5, 6, 0, 7))
print(fun(4, 8, 4, 5, e=7, f=0))

data = (2, 7, 9, 4)
print(fun(*data))
print(*data, sep='__')
print([*data])
another = {'a': 5, 'b': 7, 'c': 4, 'd': 0}
print(fun(**another))
