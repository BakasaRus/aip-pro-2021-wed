class Person:
    arms_count = 2

    def __init__(self):
        self.name = 'Test'

    def greet(self):
        print(f'Hi {self.name}!')


me = Person()
you = Person()

me.name = 'Nick'
you.name = 'Vasya'

print(me.name, you.name)
me.greet()
you.greet()

print(me.arms_count, you.arms_count)

Person.arms_count = 5
print(me.arms_count, you.arms_count)

me.age = 23
print(me.age)
