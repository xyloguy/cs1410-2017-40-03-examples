MAX_WHATEVER = 0

class Teacher:
    def __init__(self, name):
        self.name = name
        self.officehours = ''

    def getName(self):
        return self.name

    def getOfficeHours(self):
        return self.officehours

    def setOfficeHourse(self, hours):
        self.officehours = hours