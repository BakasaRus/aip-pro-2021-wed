class Person:
    arms_count = 2

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hi {self.name}!')


me = Person('Nick')
you = Person('Vasya')

print(me.name, you.name)
me.greet()
you.greet()

print(me.arms_count, you.arms_count)

Person.arms_count = 5
print(me.arms_count, you.arms_count)

me.age = 23
print(me.age)
