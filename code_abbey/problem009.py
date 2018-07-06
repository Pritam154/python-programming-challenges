'''
Problem #9: Triangles
'''


def is_triangle_possible():
    '''Returns a string for all triplets given. For each triplet,
       returns 1 if a triangle can be built with specified sides,
       returns 0 otherwise.'''
    number_cases = int(input())
    result_list = []

    for _ in range(number_cases):
        int_a, int_b, int_c = [int(x) for x in input().split()]
        # This statement needs to evaluate with '>=' to allow for triangles
        # with an area of 0.
        if (
                (int_a + int_b >= int_c) and
                (int_a + int_c >= int_b) and
                (int_b + int_c >= int_a)
        ):
            result_list.append(1)
        else:
            result_list.append(0)

    result_string = ' '.join(str(result) for result in result_list)
    return result_string


if __name__ == '__main__':
    print(is_triangle_possible())
