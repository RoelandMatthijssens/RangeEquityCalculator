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


def plus_range(hand):
    max_rank = codes_to_rank_map['A']
    min_rank = codes_to_rank_map[hand[0]]
    result = []
    while min_rank <= max_rank:
        code = rank_to_codes_map[min_rank]
        result.append(code + code)
        min_rank += 1
    return result


def parse_range(hand_range):
    result = set()

    for i in plus_range(hand_range.strip('+')):
        result.add(i)

    return sorted(list(result), key=cmp_to_key(compare_rank))
