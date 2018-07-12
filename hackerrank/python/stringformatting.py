def print_formatted(n):
    ln = len(bin(n)[2:])  # longuest_num
    sp = ' '

    for number in range(1, n+1):
        lstr = ('{} {} {} {}'
                .format(str(number).rjust(ln, sp),
                        oct(number)[2:].rjust(ln, sp),
                        hex(number)[2:].rjust(ln, sp).upper(),
                        bin(number)[2:].rjust(ln, sp)))
        print(lstr)
