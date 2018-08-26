"""Find the sum of all the multiples of 3 or 5 BELOW 1000."""

def sum_of_multiples(multiples=None, final_number=1000):
    """Returns the sum of all numbers from 1 to FINAL_NUMBER which are
    multiples found in MULTIPLES."""
    list_of_multiples = []
    if multiples is None:
        multiples = [3, 5]
    for integer in range(1, final_number):  # excludes final_number
        for multiple in multiples:
            if integer % multiple == 0:
                if integer not in list_of_multiples:
                    list_of_multiples.append(integer)
    return sum(list_of_multiples)


if __name__ == '__main__':
    result = sum_of_multiples()
    # example given: sum_of_multiples([3, 5], 10) → result = 23
    print(result)
