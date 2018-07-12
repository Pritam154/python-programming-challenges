"""
Find the Runner-Up Score!
"""


def find_runner_up():
    n = int(input())
    array_scores = [int(x) for x in input().split()]
    array_scores.sort(reverse=True)
    winner_score = array_scores[0]
    other_scores = array_scores[1:]
    runner_up_score = 0
    for value in other_scores:
        if value < winner_score:
            runner_up_score = value
            break
    return runner_up_score


if __name__ == '__main__':
    print(find_runner_up())
