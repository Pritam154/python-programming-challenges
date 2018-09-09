"""
Problem #68: Bicycle Race
"""


def find_meeting_point(dcities, sbike1, sbike2) -> float:
    """`dcities` stands for 'distance between cities'.
       `sbike1` stands for speed of bike 1.
       `sbike2` stands for speed of bike 2."""
    time_taken = dcities / (sbike1 + sbike2)
    distance_for_bike1 = sbike1 * time_taken
    return distance_for_bike1


if __name__ == '__main__':
    num_cases = int(input())
    for case in range(num_cases):
        dcities, sbike1, sbike2 = [int(x) for x in input().split()]
        print(find_meeting_point(dcities, sbike1, sbike2), end=" ")
