def solve_problem():
    n = input()
    set_s = {int(x) for x in input().split()}
    n_commands = int(input())

    for _ in range(n_commands):
        instructions = input().split()
        if 'pop' in instructions:
            try:
                set_s.pop()
            except KeyError:
                pass
        elif 'remove' in instructions:
            try:
                item = int(instructions[1])
                set_s.remove(item)
            except KeyError:
                pass
        elif 'discard' in instructions:
            item = int(instructions[1])
            set_s.discard(item)

    return sum(set_s)


if __name__ == '__main__':
    print(solve_problem())
