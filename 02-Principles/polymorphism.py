class Duck:
    def sound(self):
        print('Quack Quack!')


class Dog:
    def sound(self):
        print('Bark Bark!')


print(5 + 9)
print('Hello' + 'World')
print([8, 9] + [1, 0])

for animal in Duck(), Dog():
    animal.sound()
