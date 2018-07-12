def get_user_input():
    number_of_plants = int(input())
    list_plants_heights = {int(x) for x in input().split()}
    number_distinct_plants = len(list_plants_heights)
    return (number_distinct_plants, list_plants_heights)


def find_average_height(num_plants, list_heights):
    average_height = sum(list_heights) / num_plants
    return average_height


def main_execution():
    nb_plants, plants_heights = get_user_input()
    answer = find_average_height(nb_plants, plants_heights)
    return answer


if __name__ == '__main__':
    print(main_execution())
