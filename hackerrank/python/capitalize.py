def solve(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for index, char in enumerate(s):
        # if this is the first character in string
        if index == 0 and char in alphabet:
            char = char.upper()
        # if the character is preceded by a space
        elif char in alphabet and s[index - 1] == ' ':
            char = char.upper()
        result += char
    return result

# For testing a few test cases
# if __name__ == '__main__':
#     print(solve('132 456 Wq  m e'))
#     print(solve('hello   world  lol'))
#     print(solve('hello world'))