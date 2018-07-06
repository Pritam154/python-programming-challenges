def cycle_generator(n):
    gen_counter = 0
    height = 1
    while gen_counter < n:
        height = height * 2
        gen_counter += 1
        yield height
        height = height + 1
        gen_counter += 1
        yield height


if __name__ == '__main__':
    t = int(input())

    counter = 0
    list_height = []

    while counter != t:
        number_cycles = int(input())
        if number_cycles == 0:
            list_height.append(1)
            counter += 1
        else:
            counter_cycle = 0
            gen = cycle_generator(number_cycles)
            while counter_cycle < number_cycles:
                final_height = next(gen)
                counter_cycle += 1
            list_height.append(final_height)
            counter += 1

    for height in list_height:
        print(height)
