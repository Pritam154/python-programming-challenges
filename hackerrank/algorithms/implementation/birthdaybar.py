def get_input():
    n = int(input())
    squares = [int(x) for x in input().split()]
    d, m = [int(x) for x in input().split()]
    return (n, squares, d, m)


def count_ways(n: int, squares: list, d: int, m: int) -> int:
    current_position = 0
    end_position = m
    num_ways = 0
    max_position = len(squares) - 1
    while current_position <= max_position:
        list_to_check = squares[current_position:end_position]
        if sum(list_to_check) == d:
            num_ways += 1
        current_position += 1
        end_position += 1
    return num_ways


if __name__ == '__main__':
    n, squares, d, m = get_input()
    print(count_ways(n, squares, d, m))
