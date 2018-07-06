def countingValleys(n, s):
    nb_valleys = 0
    actual_level = 0
    under_sea = False

    for step in s:
        previous_level = actual_level
        if step == 'D':
            actual_level -= 1
        else:
            actual_level += 1

        if under_sea:
            if previous_level == -1 and actual_level == 0:
                nb_valleys += 1
                under_sea = False

        elif not under_sea:
            if previous_level == 0 and actual_level == -1:
                under_sea = True

    return nb_valleys


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
