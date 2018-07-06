def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return 'NO'
    else:
        number_of_jumps = 0
        while True:
            if x2 == x1:
                return 'YES'
            else:
                if number_of_jumps > 100000:
                    break
                else:
                    number_of_jumps += 1
                    x1 += v1
                    x2 += v2
    return 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

'''
Better approach to adapt for Python:
if(v1 > v2 && !((x2-x1)%(v1-v2)))
    printf("YES");
else
    printf("NO");
'''
