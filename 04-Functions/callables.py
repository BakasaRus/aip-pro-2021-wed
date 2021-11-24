from typing import Callable, Any


def fun(a: int, b: int) -> int:
    return a + b


def sound(being: str) -> Callable[[], str]:
    def quack() -> str:
        return 'Quack Quack'

    def default() -> str:
        return 'Test Test'

    if being == 'duck':
        return quack
    else:
        return default


def logging(f: Callable) -> Any:
    print('Calling', f)
    return f()


def greet():
    print('Hi all!')


s = fun
print(s(9, 5))

del fun

print(s(7, 2))

duck = sound('duck')
developer = sound('developer')

print(duck)
print(developer)

print(duck(), developer())

logging(greet)
