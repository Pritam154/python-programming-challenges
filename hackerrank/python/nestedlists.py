"""
Nested Lists
"""


def find_second_lowest():
    n = int(input())  # Number of students
    students_list = []

    for i in range(n):
        student_name = input()
        student_grade = float(input())
        students_list.append([student_grade, student_name])

    students_list.sort()
    lowest_grade = students_list[0][0]

    for student in students_list:
        if student[0] > lowest_grade:
            second_lowest_grade = student
            break

    second_lowest_list = []
    for student in students_list:
        if student[0] == second_lowest_grade[0]:
            second_lowest_list.append(student[1])
    second_lowest_list.sort()

    for student in second_lowest_list:
        print(student)


if __name__ == '__main__':
    find_second_lowest()
