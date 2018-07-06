if __name__ == '__main__':
    # number of birds
    n = int(input())
    all_birds = list(map(int, input().split()))
    birds_type_1 = len([bird for bird in all_birds if bird == 1])
    birds_type_2 = len([bird for bird in all_birds if bird == 2])
    birds_type_3 = len([bird for bird in all_birds if bird == 3])
    birds_type_4 = len([bird for bird in all_birds if bird == 4])
    birds_type_5 = len([bird for bird in all_birds if bird == 5])

    list_count_by_type = [birds_type_1, birds_type_2, birds_type_3,
                          birds_type_4, birds_type_5]

    max_type = []
    max_type_dict = dict()

    for type_number, type_max in enumerate(list_count_by_type):
        if type_max == max(list_count_by_type):
            max_type_dict[type_number + 1] = type_max

    print(min(max_type_dict, key=int))
