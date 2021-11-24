class Account:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount


def fun(a: int, b: int) -> int:
    return a * b


mike = Account(150)

a: int = 5
print(a)

a = 'Hello'
print(a)

print(fun(4, 5))
print(fun(4, 5.0))
print(fun(4.0, 5.0))
