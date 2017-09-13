import student

studentinfo = [
    ('Bryan', '12345678'),
    ('Jeff', '87878787')
]

students = []





for s in studentinfo:
    students.append( student.Student(s[1], s[0]) )

students[1].addClass('CS1410')
students[1].addClass('WEB1400')
students[1].addClass('ENG3010')

l1 = students[1].classes
l2 = students[1].classes

l1.append('newclass')

print(l1)
print(l2)

