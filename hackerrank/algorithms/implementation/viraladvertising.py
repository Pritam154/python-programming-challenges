'''
Viral Advertising
'''


def number_of_likes(people_reach: int) -> int:
    '''Returns the number of people who liked the advertisement
       after n days.'''
    n = int(input())
    number_likes = 0
    reach_of_day = people_reach

    for day in range(n):
        number_likes_today = reach_of_day // 2
        number_likes += number_likes_today
        reach_of_day = 3 * number_likes_today

    return number_likes


if __name__ == '__main__':
    print(number_of_likes(5))
