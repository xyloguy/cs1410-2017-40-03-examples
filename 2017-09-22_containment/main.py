from teacher import Teacher
from course import Course
from student import Student


t = Teacher('Mr. P')

cs1410 = Course()
cs1410.setTitle('CS 1410')
cs1410.setSection('03')
cs1410.setTeacher(t)

web1400 = Course()
web1400.setTitle('WEB 1400')
web1400.setSection('04')
web1400.setTeacher(t)

teacher = cs1410.getTeacher()
teacher.setOfficeHourse('M 9:00am - 9:50am')

student = Student('Arnold')
student.addCourse(cs1410)
student.addCourse(web1400)
for course in student.getCourses():
    print(course.getTeacher().getName())