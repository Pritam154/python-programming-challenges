def power_mod_power():
    int_a = int(input())
    int_b = int(input())
    int_m = int(input())

    print(pow(int_a, int_b))
    print(pow(int_a, int_b, int_m))
    return True


if __name__ == '__main__':
    power_mod_power()
