def mutate_string() -> str:
    '''Change a specific character at a given index with another given
       character and return the modified string.'''
    string_to_mutate = input()
    string_index, character_to_use = [x for x in input().split()]
    string_index = int(string_index)

    string_list = list(string_to_mutate)
    string_list[string_index] = character_to_use
    mutated_string = ''.join(string_list)

    return mutated_string


if __name__ == '__main__':
    print(mutate_string())
