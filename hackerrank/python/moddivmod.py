def mod_divmod():
    int_a = int(input())
    int_b = int(input())

    div_result = divmod(int_a, int_b)
    print(div_result[0])
    print(div_result[1])
    print(div_result)
    return True


if __name__ == '__main__':
    mod_divmod()
