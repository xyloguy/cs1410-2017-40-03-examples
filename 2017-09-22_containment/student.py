class Student:
    def __init__(self, name):
       self.name = name
       self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

    def getCourses(self):
        return self.courses