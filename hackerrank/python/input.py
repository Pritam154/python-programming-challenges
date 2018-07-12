def is_polynomial_ok():
    x, k = [int(x) for x in input().split()]
    polynomial = [x for x in input().split(" + ")]
    polynomial_f = []
    polynomial_value = 0

    for polynom in polynomial:
        if 'x' in polynom:
            string = polynom.replace('x', str(x))
            polynomial_f.append(string)
        else:
            polynomial_f.append(polynom)

    for polynom in polynomial_f:
        polynomial_value += eval(polynom)

    return polynomial_value == k


if __name__ == '__main__':
    print(is_polynomial_ok())
