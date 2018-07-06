def time_conversion(s):
    if s[-2:] == "AM":
        if s[:2] == '12':
            time_string = str('00' + s[2:8])
        else:
            time_string = s[:-2]
    else:
        if s[:2] == '12':
            time_string = s[:-2]
        else:
            time_string = str(int(s[:2]) + 12) + s[2:8]
    return time_string


if __name__ == '__main__':
    s = input()
    result = time_conversion(s)
    print(result)
