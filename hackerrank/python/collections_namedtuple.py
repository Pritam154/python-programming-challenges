from collections import namedtuple

students_marks = []
students_num = int(input())
columns_read = input()
Student = namedtuple("Student", columns_read)

for student in range(1, students_num + 1):
    si = input().split()  # student input
    student_details = Student(si[0], si[1], si[2], si[3])
    students_marks.append(float(student_details.MARKS))

average = sum(students_marks) / students_num
print('{0:.2f}'.format(average))