if __name__ == '__main__':
    if_else_number = int(input())

    if if_else_number % 2 != 0:
        print('Weird')
    else:
        if if_else_number in range(2, 6):
            print('Not Weird')
        elif if_else_number in range(6, 21):
            print('Weird')
        elif if_else_number > 20:
            print('Not Weird')
