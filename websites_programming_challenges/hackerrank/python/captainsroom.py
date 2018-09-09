def solve_problem():
    k = int(input())
    room_list = [int(x) for x in input().split()]
    room_dict = {}

    for elem in room_list:
        if elem in room_dict:
            room_dict[elem] += 1
        else:
            room_dict[elem] = 1

    for k in room_dict.keys():
        if room_dict[k] == 1:
            return k


print(solve_problem())
