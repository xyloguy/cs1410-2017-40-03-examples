class Course:
    def __init__(self):
        self.title = ''
        self.section = 0
        self.teacher = None

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getSection(self):
        return self.section

    def setSection(self, section):
        self.section = section

    def getTeacher(self):
        if self.teacher is None:
            return 'TBD'
        return self.teacher

    def setTeacher(self, teacher):
        self.teacher = teacher