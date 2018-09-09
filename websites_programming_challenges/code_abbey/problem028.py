'''
Problem #28: Body Mass Index
'''


def bmi_answer(weight, height) -> str:
    '''Calculates BMI and return a string explaining the result.
        Weight: kilograms (int)
        Height: meters (float)'''
    calculation = weight / height ** 2
    if calculation < 18.5:
        return 'under'
    elif 18.5 <= calculation < 25:
        return 'normal'
    elif 25 <= calculation < 30:
        return 'over'
    else:
        return 'obese'


NUMBER_CASES = int(input())

for i in range(NUMBER_CASES):
    input_weight, input_height = input().split()
    input_weight = int(input_weight)
    input_height = float(input_height)
    print(bmi_answer(input_weight, input_height), end=' ')
