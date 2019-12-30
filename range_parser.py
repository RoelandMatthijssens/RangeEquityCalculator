from functools import cmp_to_key, reduce

from arg_parser import parse_args
from hand import Hand
from range import Range


def range_to_hands(hand_ranges):
    ranges = [Range(i.strip()) for i in hand_ranges.split(',')]
    hands = reduce(list.__add__, [hand_range.hands for hand_range in ranges])
    unique_hands = list(set(hands))
    sorted_hands = sorted(unique_hands, key=cmp_to_key(Hand.compare))
    return sorted_hands


def parse_range(ranges):
    hands = range_to_hands(ranges)
    return [hand.value for hand in hands]


if __name__ == '__main__':
    input_range = parse_args()
    all_hands = parse_range(input_range)
    print(all_hands)
