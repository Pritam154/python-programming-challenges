def string_validation():
    input_string = input()

    string_has_alnum = False
    for char in input_string:
        if char.isalnum():
            string_has_alnum = True
            break
    print(string_has_alnum)

    string_has_alpha = False
    for char in input_string:
        if char.isalpha():
            string_has_alpha = True
            break
    print(string_has_alpha)

    string_has_digit = False
    for char in input_string:
        if char.isdigit():
            string_has_digit = True
            break
    print(string_has_digit)

    string_has_lower = False
    for char in input_string:
        if char.islower():
            string_has_lower = True
            break
    print(string_has_lower)

    string_has_upper = False
    for char in input_string:
        if char.isupper():
            string_has_upper = True
            break
    print(string_has_upper)


string_validation()


# Better way to do it...
# inp = input()
# print(any(x.isalnum() for x in inp))
# print(any(x.isalpha() for x in inp))
# print(any(x.isdigit() for x in inp))
# print(any(x.islower() for x in inp))
# print(any(x.isupper() for x in inp))
