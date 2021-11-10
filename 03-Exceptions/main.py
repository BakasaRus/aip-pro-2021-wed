def divide(a, b):
    return a / b


try:
    x, y = [int(x) for x in input().split()]
    result = divide(x, y)
    print(result)
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except ValueError as error:
    print(error)
