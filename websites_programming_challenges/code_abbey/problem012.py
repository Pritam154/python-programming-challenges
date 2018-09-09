'''
Problem #12: Modulo and time difference
'''


def timestamps_in_seconds():
    '''Returns an int that represents the difference in seconds between
       two given days.
       Problem assumes that day_2 > day_1 is always the case.'''
    timestamps = [int(x) for x in input().split()]
    day_1, hour_1 = timestamps[0], timestamps[1]
    min_1, sec_1 = timestamps[2], timestamps[3]
    day_2, hour_2 = timestamps[4], timestamps[5]
    min_2, sec_2 = timestamps[6], timestamps[7]
    timestamp_day_1 = sec_1 + 60 * min_1 + 3600 * hour_1 + 86400 * day_1
    timestamp_day_2 = sec_2 + 60 * min_2 + 3600 * hour_2 + 86400 * day_2
    timestamp_difference = timestamp_day_2 - timestamp_day_1
    return timestamp_difference


def timestamps_in_days(timestamp_seconds):
    '''Returns a string converting a timestamp in seconds back to its
       meaningful interpretation in days, hours, minutes and seconds.'''
    number_days = timestamp_seconds // 86400
    remainder_days = timestamp_seconds % 86400
    number_hours = remainder_days // 3600
    remainder_hours = remainder_days % 3600
    number_minutes = remainder_hours // 60
    number_seconds = remainder_hours % 60
    timestamps_days = '({} {} {} {})'.format(number_days, number_hours,
                                             number_minutes, number_seconds)
    return timestamps_days


def execute_program():
    '''Returns a string as a final answer, using above functions and
       looping for the number of times required by the problem.'''
    number_cases = int(input())
    result_list = []

    for _ in range(number_cases):
        time_difference = timestamps_in_seconds()
        time_in_days = timestamps_in_days(time_difference)
        result_list.append(time_in_days)

    final_answer = ' '.join(str(answer) for answer in result_list)
    return final_answer


if __name__ == '__main__':
    print(execute_program())
