class PowTwelve:
    __cur_pow: int
    __max_pow: int

    def __init__(self, max_pow: int) -> None:
        self.__max_pow = max_pow
        self.__cur_pow = 0

    def __iter__(self) -> 'PowTwelve':
        return self

    def __next__(self):
        if self.__cur_pow > self.__max_pow:
            raise StopIteration

        res = 12 ** self.__cur_pow
        self.__cur_pow += 1
        return res


for item in PowTwelve(5):
    print(item)
