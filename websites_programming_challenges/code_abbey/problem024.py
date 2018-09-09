def next_seq(number: int) -> int:
    result = int(number) ** 2
    result = '{0:0>8}'.format(result)
    result = int(result[2:6])
    return result


def count_newmann(number: int) -> int:
    loop_count = 0
    loop_list = [number]
    while len(set(loop_list)) == len(loop_list):
        next_num = next_seq(loop_list[-1])
        loop_list.append(next_num)

    return len(loop_list) - 1


if __name__ == '__main__':
    nb_elements = int(input())
    elements = [int(x) for x in input().split()]

    for elem in elements:
        print(count_newmann(elem), end=' ')
