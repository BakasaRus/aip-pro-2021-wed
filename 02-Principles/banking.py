class Account:
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    # @amount.setter
    # def amount(self, amount):
    #     self.__amount = amount

    def transfer(self, other, to_transfer):
        if self.__amount - to_transfer >= 0:
            self.__amount -= to_transfer
            other.__amount += to_transfer


nick = Account(50)
mike = Account(150)

print(nick.amount, mike.amount)
nick.transfer(mike, 500)
print(nick.amount, mike.amount)
