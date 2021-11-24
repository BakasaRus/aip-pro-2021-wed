from typing import Generator


def pow_twelve(max_pow: int) -> Generator:
    cur_pow: int = 0
    while cur_pow <= max_pow:
        yield 12 ** cur_pow
        cur_pow += 1


for item in pow_twelve(5):
    print(item)
