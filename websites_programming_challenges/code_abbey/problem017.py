def array_checksum(array_list):
    """Returns checksum of a list of integers."""
    array_length = len(array_list)
    result = i = 0
    seed = 113
    limit = 10000007

    while i < array_length:
        result = (result + array_list[i]) * seed
        if result > limit:
            result %= limit
        i += 1

    return result


if __name__ == '__main__':
    array_number = int(input())  # captured but not used
    array_list = [int(x) for x in input().split()]
    print(array_checksum(array_list))
