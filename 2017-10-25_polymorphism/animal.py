class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        raise NotImplementedError('speak() must be implemented in the child class')


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, 'cat')

    def speak(self):
        return 'I am ' + self.name + ' meow.'


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, 'dog')

    def speak(self):
        return 'woof'

dog = Animal('Tweety', 'bird')
cat = Cat('Garfield')
bird = Dog('Odie')

print(dog.name, dog.breed)
print(cat.speak())
print(bird.speak())
