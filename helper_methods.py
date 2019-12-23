from .hand import Hand


def compare_rank(a, b):
    rank_11 = Hand.codes_to_rank_map[a[0]]
    rank_12 = Hand.codes_to_rank_map[a[1]]
    rank_21 = Hand.codes_to_rank_map[b[0]]
    rank_22 = Hand.codes_to_rank_map[b[1]]
    if rank_11 > rank_21: return -1
    if rank_21 > rank_11: return 1
    if rank_12 > rank_22: return -1
    if rank_22 > rank_12: return 1


def flatten(l):
    return [i for sub_l in l for i in sub_l]
