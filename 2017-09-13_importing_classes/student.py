class Student:
    def __init__(self, id, name):
        self.blajsdfhsdfjsdfjh = id
        self.__name = name
        self.classes = []

    def getName(self):
        return self.__name

    def getID(self):
        return self.blajsdfhsdfjsdfjh

    def setID(self, newid):
        if len(str(newid)) == 8:
            self.blajsdfhsdfjsdfjh = newid

    def addClass(self, c):
        self.classes.append(c)
