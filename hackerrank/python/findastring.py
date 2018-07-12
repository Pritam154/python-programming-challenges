def find_a_string() -> int:
    initial_string = input()
    substring_to_find = input()
    modified_string = initial_string[:]  # makes a copy of initial_string
    substring_count = 0
    substring_length = len(substring_to_find)

    # Moves to the beginning of the next occurrence of substring
    position_modifier = substring_length - 1

    # If we don't adjust for substring of length == 1, the following loop
    # becomes infinite as we never move in the modified_string
    if substring_length == 1:
        position_modifier = 1

    while substring_to_find in modified_string:
        # Gives the index where a match is found. There is always a match,
        # as the loop will have broken otherwise.
        substring_match = modified_string.find(substring_to_find)

        substring_count += 1
        new_position = substring_match + position_modifier

        # when new_position is greater than last index position in
        # modified_string, it becomes an empty string and while loop is broken
        modified_string = modified_string[new_position:]

    return substring_count


if __name__ == '__main__':
    print(find_a_string())
