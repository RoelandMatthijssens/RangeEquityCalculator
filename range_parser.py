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


def min_to_max(a, b):
    rank_a = codes_to_rank_map[a[0]]
    rank_b = codes_to_rank_map[b[0]]
    top = max(rank_a, rank_b)
    bottom = min(rank_a, rank_b)
    result = []
    while bottom <= top:
        code = rank_to_codes_map[bottom]
        result.append(code + code)
        bottom += 1
    return result


def is_plus_range(hand_range):
    return '+' in hand_range


def plus_range(hand_range):
    return min_to_max('AA', hand_range)


def is_dash_range(hand_range):
    return '-' in hand_range


def single_hand(hand_range):
    return hand_range


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
