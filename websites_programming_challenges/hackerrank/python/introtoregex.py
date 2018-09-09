def is_valid_float(value: str) -> bool:
    try:
        new_value = float(value)  # if it throws an error, type is incorrect
        if value.find(".") == -1:  # if there is no dot, it is not a float
            return False
        elif value.endswith("."):
            return False  # float needs a decimal value in this case
        else:
            return True
    except ValueError:
        return False


if __name__ == '__main__':
    nb_tests = int(input())
    for test in range(nb_tests):
        print(is_valid_float(input()))
