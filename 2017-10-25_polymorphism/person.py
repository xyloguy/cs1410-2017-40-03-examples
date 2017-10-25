import random
class Person:
    def __init__(self, name):
        self.name = name
        self.dob = None

    def set_dob(self, dob):
        self.dob = dob

    def pay_bills(self):
        raise NotImplementedError()


class Student(Person):
    def __init__(self, name, sid):
        Person.__init__(self, name)
        self.id = sid
        self.classes = []

    def add_class(self, course):
        self.classes.append(course)

    def pay_bills(self):
        return 'Hi, I am ' + self.name + '. Can I wash your dishes?'


class Undergrad(Student):
    def pay_bills(self):
        return 'Looks like raman tonight'


class Teacher(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def pay_bills(self):
        return 'I have just enough.'


class Millionaire(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def pay_bills(self):
        return 'Keep the change.'

people = [
    Millionaire('Bill'),
    Teacher('Mr. C'),
    Student('Sally', '1234'),
    Undergrad('Janet', '2345'),
]

for p in people:
    month = random.randint(1,12)
    day = random.randint(1,28)
    year = random.randint(1958, 2009)
    dob = str(month) + '/' + str(day) + '/' + str(year)
    p.set_dob(dob)
    print(p.name, p.dob, p.pay_bills())


