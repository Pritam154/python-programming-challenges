'''
Cut The Sticks
'''


def cut_sticks():
    n = int(input())
    sticks_list = [int(x) for x in input().split()]

    print(n)

    while len(sticks_list) > 1:
        new_sticks_list = []
        smallest_stick = min(sticks_list)
        for stick in sticks_list:
            stick_length = stick - smallest_stick
            if stick_length != 0:
                new_sticks_list.append(stick_length)
        sticks_list = new_sticks_list

        list_length = len(sticks_list)
        if list_length >= 1:
            print(list_length)


if __name__ == '__main__':
    cut_sticks()
