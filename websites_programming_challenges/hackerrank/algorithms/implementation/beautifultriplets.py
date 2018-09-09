def beautifulTriplets(d, arr):
    triplets_count = 0
    for value in arr:
        triplet2 = value + d
        triplet3 = triplet2 + d
        triplets = [value, triplet2, triplet3]
        triplets_are_in_arr = (triplet in arr for triplet in triplets)
        if all(triplets_are_in_arr):
            triplets_count += 1
    return triplets_count


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    arr = list(map(int, second_line.split()))
    result = beautifulTriplets(d, arr)
    print(result)
