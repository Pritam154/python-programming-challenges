if __name__ == '__main__':
    number_of_grades = int(input())  # Number of grades to evaluate
    list_of_grades = []  # Used to make a list out of all grades to evaluate

    # Add all the grades to the above list
    for i in range(number_of_grades):
        grade = int(input())
        list_of_grades.append(grade)

    # Make a new list to list all the final grades after their evaluation
    list_final_grades = []

    # Test every grade and adjust its final score
    for grade in list_of_grades:
        if grade >= 38:
            last_digit_in_grade = (str(grade))[-1]
            if last_digit_in_grade == '3' or last_digit_in_grade == '8':
                grade += 2
            elif last_digit_in_grade == '4' or last_digit_in_grade == '9':
                grade += 1
            list_final_grades.append(grade)
        else:
            list_final_grades.append(grade)

    # Print every final grade on a new line
    for grade in list_final_grades:
        print(grade)
