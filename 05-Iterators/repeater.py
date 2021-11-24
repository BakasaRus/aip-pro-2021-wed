from typing import Any


class Repeater:
    __value: Any

    def __init__(self, value: Any) -> None:
        self.__value = value

    def __iter__(self) -> 'Repeater':
        return self

    def __next__(self):
        return self.__value


for item in Repeater(5):
    print(item)
