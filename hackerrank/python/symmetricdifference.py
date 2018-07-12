def solve_problem():
    int_m = int(input())
    m_integers = {int(x) for x in input().split()}
    int_n = int(input())
    n_integers = {int(x) for x in input().split()}
    list_all_differences = []

    for integer in m_integers.difference(n_integers):
        list_all_differences.append(integer)
    for integer in n_integers.difference(m_integers):
        list_all_differences.append(integer)

    list_all_differences.sort()

    for integer in list_all_differences:
        print(integer)

    return True


if __name__ == '__main__':
    solve_problem()
