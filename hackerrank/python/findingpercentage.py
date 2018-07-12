'''
Finding the Percentage
'''


def find_student_average():
    n = int(input())
    students_dic = {}

    for i in range(n):
        student_details = [x for x in input().split()]
        student_name = student_details[0]
        student_marks = [float(x) for x in student_details[1:]]
        students_dic[student_name] = student_marks

    student_to_average = input()

    marks_to_average = students_dic[student_to_average]
    number_of_marks = len(marks_to_average)
    sum_of_marks = sum(marks_to_average)
    average_of_marks = sum_of_marks / number_of_marks
    rounded_average = '{0:.2f}'.format(average_of_marks)  # Gives 2 decimals

    return rounded_average


if __name__ == '__main__':
    print(find_student_average())
