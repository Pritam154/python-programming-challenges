if __name__ == '__main__':
    # Fix the area covered by Sam's house from input
    # s = Starting position on 'x' axis
    # t = Ending position on 'x' axis
    s, t = list(map(int, input().split()))

    # Fix the position of the trees near Sam's house from input
    # a = Apple tree, b = Orange tree
    a, b = list(map(int, input().split()))

    # Fix the number of fruits falling from each tree
    # m = Number of apples, n = Number of oranges
    m, n = list(map(int, input().split()))

    # For all apples, list the distance the fruit fall from the tree
    falling_apples = list(map(int, input().split()))

    # For all oranges, list the distance the fruit fall from the tree
    falling_oranges = list(map(int, input().split()))

    apples_falling_on_house = 0
    oranges_falling_on_house = 0

    for apple in falling_apples:
        apple_distance = (a + apple)
        if s <= apple_distance <= t:
            apples_falling_on_house += 1

    for orange in falling_oranges:
        orange_distance = (b + orange)
        if s <= orange_distance <= t:
            oranges_falling_on_house += 1

    print(apples_falling_on_house)
    print(oranges_falling_on_house)
