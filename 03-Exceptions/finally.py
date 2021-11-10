def fun(a, b):
    try:
        if a > 0:
            return a + b
        else:
            raise ValueError
    except ValueError:
        return 0
    finally:
        return -1


print(fun(8, 3))
print(fun(0, 5))
print(fun("awfasdf", 'sadfsadfdf'))
