def read_input():
    n_clouds = int(input())
    cloud_values = [int(x) for x in input().split()]
    cloud_dict = {}

    for cloud_index in range(n_clouds):
        for value in cloud_values:
            cloud_dict[cloud_index] = value
            cloud_values.remove(value)
            break

    return (n_clouds, cloud_dict)


def solve_clouds():
    n_clouds, cloud_dict = read_input()
    last_cloud = n_clouds - 1
    current_position = 0
    nb_jumps = 0

    while True:
        if current_position == last_cloud:
            break
        try:
            if cloud_dict[current_position+2] == 0:
                current_position += 2
            else:
                current_position += 1
        except KeyError:
            current_position += 1
        nb_jumps += 1

    return nb_jumps


if __name__ == '__main__':
    print(solve_clouds())
