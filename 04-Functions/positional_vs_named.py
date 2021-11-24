def fun(a, b, c):
    return a + b + c


print(fun(3, 7, 5))
print(fun(3, b=7, c=5))
print(fun(b=7, c=5, a=3))
print(fun(a=3, 7, 5))
