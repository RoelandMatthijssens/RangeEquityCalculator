from functools import cmp_to_key, reduce

from .helper_methods import compare_rank
from .range import Range


def compose(*functions):
    """compose many functions into one"""

    def compose_two(f, g):
        return lambda x: f(g(x))

    return reduce(compose_two, functions, lambda x: x)


def parse_range(ranges):
    hands = set()
    for sub_range in ranges.split(','):
        hands = hands.union(Range(sub_range.strip()).hands)

    return sorted(list(hands), key=cmp_to_key(compare_rank))
