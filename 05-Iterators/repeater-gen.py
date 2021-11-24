from typing import Any, Generator


def repeater(value: Any) -> Generator:
    while True:
        yield value


for item in repeater(5):
    print(item)
