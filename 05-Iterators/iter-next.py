numbers = [5, 7, 0]

iterator = iter(numbers)

while True:
    try:
        a = next(iterator)
        print(a)
    except StopIteration:
        break

for item in numbers:
    print(item)
