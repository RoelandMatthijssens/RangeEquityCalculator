from functools import cmp_to_key

from .hand import Hand
from .helper_methods import flatten
from .range import Range


def parse_range(ranges):
    ranges = [Range(i.strip()) for i in ranges.split(',')]
    hands = flatten([hand_range.hands for hand_range in ranges])
    unique_hands = list(set(hands))
    sorted_hands = sorted(unique_hands, key=cmp_to_key(Hand.compare))
    return [hand.value for hand in sorted_hands]
