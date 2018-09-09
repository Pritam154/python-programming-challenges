def solve_problem():
    a_num = int(input())
    set_a = {int(x) for x in input().split()}
    n = int(input())

    for _ in range(n):
        input_command = input().split()
        input_operation = input_command[0]
        input_len_set = int(input_command[1])
        set_b = {int(x) for x in input().split()}
        if input_operation == 'update':
            set_a.update(set_b)
        elif input_operation == 'intersection_update':
            set_a.intersection_update(set_b)
        elif input_operation == 'difference_update':
            set_a.difference_update(set_b)
        elif input_operation == 'symmetric_difference_update':
            set_a.symmetric_difference_update(set_b)
    return sum(set_a)


if __name__ == '__main__':
    print(solve_problem())
