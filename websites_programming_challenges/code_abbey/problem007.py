'''
Problem #7: Fahrenheit to Celsius
'''


def fahrenheit_to_celsius(temperature):
    '''Simple function that converts temperatures from Fahrenheit
       to Celsius and rounds the answer to the nearest integer.'''
    return round((temperature - 32) * 5 / 9)


def execute_problem():
    '''Reads all the data from the problem and
       returns a string of temperatures.'''
    all_data = [int(x) for x in input().split()]
    temp_values = all_data[1:]
    converted_values = []

    for value in temp_values:
        converted_value = fahrenheit_to_celsius(value)
        converted_values.append(converted_value)

    result_string = ' '.join(str(result) for result in converted_values)
    return result_string


if __name__ == '__main__':
    print(execute_problem())
