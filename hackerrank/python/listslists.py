def read_list():
    n = int(input())
    list_n = []
    for i in range(n):
        cmd_pos = input().split()
        try:
            cmd_pos[1] = int(cmd_pos[1])
            cmd_pos[2] = int(cmd_pos[2])
        except IndexError:
            pass
        if cmd_pos[0] == 'insert':
            list_n.insert(cmd_pos[1], cmd_pos[2])
        elif cmd_pos[0] == 'print':
            print(list_n)
        elif cmd_pos[0] == 'remove':
            list_n.remove(cmd_pos[1])
        elif cmd_pos[0] == 'append':
            list_n.append(cmd_pos[1])
        elif cmd_pos[0] == 'sort':
            list_n.sort()
        elif cmd_pos[0] == 'pop':
            list_n.pop()
        elif cmd_pos[0] == 'reverse':
            list_n.reverse()


if __name__ == '__main__':
    read_list()
