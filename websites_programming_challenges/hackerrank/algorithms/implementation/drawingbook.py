def page_turns() -> int:
    nb_pages = int(input())
    page_nb = int(input())
    book = [(1,)]
    middle_book = nb_pages // 2

    if nb_pages == 2:
        book.append((2,))

    if nb_pages % 2 == 0 and nb_pages > 2:
        for p_num in range(2, nb_pages, 2):
            book.append((p_num, p_num+1))
        book.append((nb_pages,))

    if nb_pages % 2 != 0 and nb_pages > 2:
        for p_num in range(2, nb_pages+1, 2):
            book.append((p_num, p_num+1))

    if page_nb > middle_book:
        book.sort(reverse=True)

    for index, pages in enumerate(book):
        if page_nb in pages:
            return index


if __name__ == '__main__':
    print(page_turns())
