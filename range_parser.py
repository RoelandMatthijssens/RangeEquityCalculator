from functools import cmp_to_key

codes_to_rank_map = {
    '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
    'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12
}
rank_to_codes_map = {
    0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9',
    8: 'T', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'
}


def compare_rank(h1, h2):
    h11 = codes_to_rank_map[h1[0]]
    h12 = codes_to_rank_map[h1[1]]
    h21 = codes_to_rank_map[h2[0]]
    h22 = codes_to_rank_map[h2[1]]
    if h11 > h21: return -1
    if h21 > h11: return 1
    if h12 > h22: return -1
    if h22 > h12: return 1


def min_to_max_connectors_and_gappers(a, b):
    rank_11 = codes_to_rank_map[a[0]]
    rank_21 = codes_to_rank_map[b[0]]
    rank_22 = codes_to_rank_map[b[1]]
    result = []
    while rank_11 >= rank_21:
        hand = rank_to_codes_map[rank_21] + rank_to_codes_map[rank_22]
        result.append(hand)
        rank_21 += 1
        rank_22 += 1
    return result


def min_to_max(a, b):
    if a[0] == a[1] and b[0] == b[1]:
        return min_to_max_pairs(a, b)
    elif a[0] == b[0] and a[1] != b[1]:
        return min_to_max_non_pairs(a, b)
    else:
        return min_to_max_connectors_and_gappers(a, b)


def min_to_max_pairs(a, b):
    rank_a = codes_to_rank_map[a[0]]
    rank_b = codes_to_rank_map[b[0]]
    top = max(rank_a, rank_b)
    bottom = min(rank_a, rank_b)
    return [rank_to_codes_map[i] * 2 for i in range(bottom, top + 1)]


def min_to_max_non_pairs(a, b):
    rank_12 = codes_to_rank_map[a[1]]
    rank_22 = codes_to_rank_map[b[1]]
    min_rank_2 = min(rank_12, rank_22)
    max_rank_2 = max(rank_12, rank_22)
    return [a[0] + rank_to_codes_map[i] for i in range(min_rank_2, max_rank_2 + 1)]


def is_plus_range(hand_range):
    return '+' in hand_range


def plus_range(hand_range):
    a = hand_range[0]
    b = hand_range[1]
    if a == b:
        return min_to_max('AA', hand_range)
    else:
        rank_a = codes_to_rank_map[a]
        rank_b = codes_to_rank_map[b]
        highest_card = max(rank_a, rank_b)
        lowest_card = min(rank_a, rank_b)
        # A7 gets transformed to AK-A7
        top_hand = rank_to_codes_map[highest_card] + rank_to_codes_map[highest_card - 1]
        bottom_hand = rank_to_codes_map[highest_card] + rank_to_codes_map[lowest_card]
        return min_to_max(bottom_hand, top_hand)


def is_dash_range(hand_range):
    return '-' in hand_range


def single_hand(hand_range):
    low_card = min(codes_to_rank_map[hand_range[0]], codes_to_rank_map[hand_range[1]])
    high_card = max(codes_to_rank_map[hand_range[0]], codes_to_rank_map[hand_range[1]])
    return rank_to_codes_map[high_card] + rank_to_codes_map[low_card]


def dash_range(hand_range):
    top, bottom = hand_range.split('-')
    return min_to_max(top, bottom)


def parse_sub_range(sub_range):
    result = set()

    if is_plus_range(sub_range):
        for i in plus_range(sub_range.strip('+')):
            result.add(i)
    elif is_dash_range(sub_range):
        for i in dash_range(sub_range):
            result.add(i)
    else:
        result.add(single_hand(sub_range))

    return result


def parse_range(hand_range):
    result = set()

    for sub_range in hand_range.split(','):
        result = result.union(parse_sub_range(sub_range.strip()))

    return sorted(list(result), key=cmp_to_key(compare_rank))
