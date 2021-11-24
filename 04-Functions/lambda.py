from random import randint

numbers = [randint(-50, 50) for x in range(10)]
print(*numbers)
numbers.sort(key=lambda x: x ** 2)
print(*numbers)

print(*filter(lambda x: x >= -10, numbers))
