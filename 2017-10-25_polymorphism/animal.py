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


class TweetyBird(Animal):
    def __init__(self):
        Animal.__init__(self, 'Tweety', 'bird')

    def speak(self):
        return 'I tought I saw a putty cat.'


dog = TweetyBird()
cat = Cat('Garfield')
bird = Dog('Odie')

print(dog.name, dog.breed)
print(dog.speak())
print(cat.speak())
print(bird.speak())
