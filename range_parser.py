from functools import cmp_to_key, reduce

from .helper_methods import compare_rank, flatten
from .range import Range


def compose(*functions):
    """compose many functions into one"""

    def compose_two(f, g):
        return lambda x: f(g(x))

    return reduce(compose_two, functions, lambda x: x)


def parse_range(ranges):
    ranges = [Range(i.strip()) for i in ranges.split(',')]
    hands = flatten([hand_range.hands for hand_range in ranges])
    unique_hands = list(set([hand.value for hand in hands]))
    sorted_hands = sorted(unique_hands, key=cmp_to_key(compare_rank))
    return sorted_hands
