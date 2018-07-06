def min_distance():
    nb_values = int(input())
    values = [int(x) for x in input().split()]
    position = 0
    list_pairs = []
    max_position = len(values) - 1

    while position <= max_position:
        for index, value in enumerate(values):
            if values[position] == value and index != position:
                rel_distance = abs(position - index)
                list_pairs.append(rel_distance)
        position += 1

    if list_pairs == []:
        return -1
    else:
        return min(list_pairs)


if __name__ == '__main__':
    print(min_distance())
