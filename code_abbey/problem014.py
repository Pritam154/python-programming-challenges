last_answer = int(input())

while True:
    last_line = input().split()

    if last_line[0] == '+':
        last_answer = last_answer + int(last_line[1])

    if last_line[0] == '*':
        last_answer = last_answer * int(last_line[1])

    if last_line[0] == '%':
        last_answer = last_answer % int(last_line[1])
        break

print(last_answer)


'''
Better implementation:

num = int(input())
while True:
    operator, number = input().split()
    number = int(number)
    if operator == '%':
        num %= number
        break
    elif operator == '+':
        num += number
    elif operator == '*':
        num *= number

print(num)
'''