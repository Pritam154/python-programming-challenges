def find_polar_coordinates():
    import cmath
    coordinates = cmath.polar(complex(input()))
    print(coordinates[0])
    print(coordinates[1])
    return True


if __name__ == '__main__':
    find_polar_coordinates()
