import textwrap


def wrap(string, max_width):
    return textwrap.wrap(string, max_width)


def execute():
    string = input()
    max_width = int(input())
    list_wrap = wrap(string, max_width)
    for line in list_wrap:
        print(line)


if __name__ == '__main__':
    execute()
