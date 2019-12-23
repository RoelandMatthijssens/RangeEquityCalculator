from .hand import Hand


class Range():
    def __init__(self, hand_range):
        self.range_string = hand_range
        self.hands = self.explode_range()

    def explode_range(self):
        if self.is_plus_range():
            return self.plus_range()
        elif self.is_dash_range():
            return self.dash_range()
        else:
            return [self.single_hand()]

    def is_plus_range(self):
        return '+' in self.range_string

    def is_dash_range(self):
        return '-' in self.range_string

    def plus_range(self):
        hand = Hand(self.range_string.strip('+'))
        if hand.is_pair():
            hands = self.min_to_max_hands(Hand('AA'), hand)
        else:
            top_hand = Hand.from_ranks(hand.max_rank, hand.max_rank - 1)
            bottom_hand = Hand.from_ranks(hand.max_rank, hand.min_rank)
            hands = self.min_to_max_hands(bottom_hand, top_hand)
        return hands

    def dash_range(self):
        top, bottom = [Hand(i) for i in self.range_string.split('-')]
        return self.min_to_max_hands(top, bottom)

    def single_hand(self):
        return Hand(self.range_string)

    def min_to_max_hands(self, a, b):
        if a.is_pair() and b.is_pair():
            return self.min_to_max_pairs(a, b)
        elif a.max_rank == b.max_rank and a.min_rank != b.min_rank:
            return self.min_to_max_non_pairs(a, b)
        else:
            return self.min_to_max_connectors_and_gappers(a, b)

    @staticmethod
    def min_to_max_connectors_and_gappers(a, b):
        delta = b.max_rank - b.min_rank
        return [Hand.from_ranks(i, i - delta) for i in range(b.max_rank, a.max_rank + 1)]

    @staticmethod
    def min_to_max_pairs(a, b):
        top = max(a.max_rank, b.max_rank)
        bottom = min(a.max_rank, b.max_rank)
        return [Hand.from_ranks(i, i) for i in range(bottom, top + 1)]

    @staticmethod
    def min_to_max_non_pairs(a, b):
        min_rank_2 = min(a.min_rank, b.min_rank)
        max_rank_2 = max(a.min_rank, b.min_rank)
        return [Hand.from_ranks(a.max_rank, i) for i in range(min_rank_2, max_rank_2 + 1)]
