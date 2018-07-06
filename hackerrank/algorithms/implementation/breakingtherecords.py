if __name__ == '__main__':
    number_of_games = int(input())
    list_of_scores = list(map(int, input().split()))

    broken_best_record = list_of_scores[0]
    broken_worst_record = list_of_scores[0]

    number_broken_best = 0
    number_broken_worst = 0

    for score in list_of_scores[1:]:
        if score > broken_best_record:
            number_broken_best += 1
            broken_best_record = score
        if score < broken_worst_record:
            number_broken_worst += 1
            broken_worst_record = score

    print(number_broken_best, number_broken_worst)
