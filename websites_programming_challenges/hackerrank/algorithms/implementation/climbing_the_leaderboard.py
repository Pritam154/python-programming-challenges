# FIXME: This works but it is too slow.


from collections import defaultdict


def get_leaderboard(current_scores: list) -> dict:
    current_scores.sort()
    record = 0
    leader_dict = defaultdict(list)

    while len(current_scores) > 0:
        max_value = max(current_scores)
        num_max = current_scores.count(max_value)

        if 1 not in leader_dict:
            for i in range(num_max):
                leader_dict[1].append(max_value)
                current_scores.remove(max_value)
        else:
            next_rank = max(leader_dict) + 1
            for i in range(num_max):
                leader_dict[next_rank].append(max_value)
                current_scores.remove(max_value)

    return leader_dict


# without duplicates, just check current position without [0]
def get_new_position(num_scores: int, game_score: int,
                     leader_dict: dict) -> int:
    current_position = 1
    while current_position <= num_scores:
            if game_score >= leader_dict[current_position][0]:
                return current_position
            else:
                current_position += 1

    return current_position


if __name__ == '__main__':
    num_scores = int(input())
    lst_scores = [int(x) for x in input().split()]
    num_games = int(input())
    lst_games = [int(x) for x in input().split()]
    leaders = get_leaderboard(lst_scores)
    num_positions = len(leaders)

    for game in lst_games:
        print(get_new_position(num_positions, game, leaders))
