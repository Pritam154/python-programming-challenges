def find_angle_mbc():
    import math
    len_ab = int(input())
    len_bc = int(input())
    hypotenuse = math.sqrt(len_ab**2 + len_bc**2)
    cos_angle = len_bc / hypotenuse
    angle_degrees = math.acos(cos_angle)*180/math.pi  # Converts from radians

    angle_str = str(angle_degrees).split(".")
    angle_str = int(angle_str[1][0])  # Get first digit after decimal point

    if angle_str < 5:
        return round(angle_degrees)
    else:
        return math.ceil(angle_degrees)


if __name__ == '__main__':
    print('{}°'.format(find_angle_mbc()))
