def palindrome(s):
    def strip_string(s):
        new_string = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        s = s.lower()
        for char in s:
            if char in alphabet:
                new_string += char
        return new_string

    def is_palindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_palindrome(s[1:-1])
    if is_palindrome(strip_string(s)):
        return 'Y'
    else:
        return 'N'


number_of_cases = int(input())
palindrome_list = []

[palindrome_list.append(palindrome(input())) for i in range(number_of_cases)]
[print(i, end=' ') for i in palindrome_list]
