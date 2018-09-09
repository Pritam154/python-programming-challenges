"""
5 3 → n, k
4 2 6 1 10 → arr
"""


def return_chapter(k, np, chapters_dict):
    """k = problems/page, np = total_number_problems"""
    problem = 1
    while problem <= np:
        if len(chapters_dict[max(chapters_dict)]) < k:
            chapters_dict[max(chapters_dict)] = (
                chapters_dict[max(chapters_dict)] + [problem])
        else:
            chapters_dict[max(chapters_dict)+1] = [problem]
        problem += 1
    chapters_dict[max(chapters_dict)+1] = []  # start new page for next chapter
    return chapters_dict


def count_magic_problems(book_dict):
    counter = 0
    for key, value in book_dict.items():
        if key in value:
            counter += 1
    return counter


def workbook(n, k, arr):
    """n = chapters, k = problems/page, arr = problems/chapter"""
    chapters_dict = {1: []}
    for chapter in arr:
        chapters_dict = return_chapter(k, chapter, chapters_dict)
    return count_magic_problems(chapters_dict)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)
