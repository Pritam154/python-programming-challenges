def matching_pairs() -> int:
    nb_socks = int(input())
    all_socks = [int(x) for x in input().split()]
    nb_pairs = 0

    while len(all_socks) > 0:
        sock = all_socks.pop()
        if sock in all_socks:
            all_socks.remove(sock)
            nb_pairs += 1

    return nb_pairs


if __name__ == '__main__':
    print(matching_pairs())
