def solve_problem():
    n = int(input())
    n_students = {int(x) for x in input().split()}
    b = int(input())
    b_students = {int(x) for x in input().split()}

    n_b_total = n_students.intersection(b_students)
    return len(n_b_total)


if __name__ == '__main__':
    print(solve_problem())
