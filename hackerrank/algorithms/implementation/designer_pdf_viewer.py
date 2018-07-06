import string


def designerPdfViewer(h, word):
    alpha_string = string.ascii_lowercase
    alpha_dict = {alpha_string[x]: h[x] for x in range(26)}
    length_word = len(word)

    highest = 0
    for letter in word:
        letter_value = alpha_dict[letter]
        if letter_value > highest:
            highest = letter_value

    return(highest*length_word)


if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
