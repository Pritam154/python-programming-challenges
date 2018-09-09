'''
Problem #22: Names scores
'''

import string

WORKING_FILE = 'problem22_names.txt'
ALPHABET_SCORE = {}


def read_problem_data(data_file) -> list:
    with open(data_file, 'r') as nf:
        read_data = nf.read()
        read_data = read_data.replace('"', '')
        data_read = [string for string in read_data.split(",")]
        data_read.sort()
    return data_read


def fix_alphabet(dictionary):
    alphabet = string.ascii_lowercase
    for index, letter in enumerate(alphabet):
        dictionary[letter] = index + 1
    return dictionary


def score_word(name, position, dictionary):
    name_score = 0
    for letter in name:
        name_score += dictionary[letter]
    word_score = name_score * (position + 1)
    return word_score


def execute_program():
    '''Adding a docstring. Let's see the difference with pydoc3.'''
    fix_alphabet(ALPHABET_SCORE)
    data = read_problem_data(WORKING_FILE)
    total_score = 0
    for index, word in enumerate(data):
        total_score += score_word(word, index, ALPHABET_SCORE)
    return total_score


print(execute_program())
