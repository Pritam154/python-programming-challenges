import os


def serviceLane(width, cases):
    return [min(width[x:y+1]) for x, y in cases]


if __name__ == '__main__':
    nt = input().split()
    n = int(nt[0])
    t = int(nt[1])
    width = list(map(int, input().rstrip().split()))
    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)
    print(result)
