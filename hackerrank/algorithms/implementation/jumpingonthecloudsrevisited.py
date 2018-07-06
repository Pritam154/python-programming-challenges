'''
Jumping on the Clouds: Revisited
'''


def solve_energy_left(energy=100) -> int:
    '''Returns the amount of energy left after all the jumps.'''
    n, k = [int(x) for x in input().split()]
    cloud_values = [int(x) for x in input().split()]
    cloud_dict = {}
    for cloud_index in range(n):
        for value in cloud_values:
            cloud_dict[cloud_index] = value
            cloud_values.remove(value)
            break

    number_jumps = n // k
    for jump in range(1, number_jumps + 1):
        cloud_index = jump * k
        if cloud_index == n:
            cloud_index = 0

        if cloud_dict[cloud_index] == 0:
            energy -= 1
        else:
            energy -= 3

    print(energy)


if __name__ == '__main__':
    solve_energy_left()
