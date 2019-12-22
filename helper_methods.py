from .range import Range


def compare_rank(a, b):
    rank_11 = Range.codes_to_rank_map[a[0]]
    rank_12 = Range.codes_to_rank_map[a[1]]
    rank_21 = Range.codes_to_rank_map[b[0]]
    rank_22 = Range.codes_to_rank_map[b[1]]
    if rank_11 > rank_21: return -1
    if rank_21 > rank_11: return 1
    if rank_12 > rank_22: return -1
    if rank_22 > rank_12: return 1
