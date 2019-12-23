class Hand():
    codes_to_rank_map = {
        '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
        'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12
    }
    rank_to_codes_map = {
        0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9',
        8: 'T', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'
    }

    def __init__(self, hand_string=None):
        if hand_string:
            self.from_codes(hand_string)

    @classmethod
    def from_ranks(cls, a, b):
        return cls(cls.rank_to_codes_map[a] + cls.rank_to_codes_map[b])

    def from_codes(self, codes):
        rank_1 = Hand.codes_to_rank_map[codes[0]]
        rank_2 = Hand.codes_to_rank_map[codes[1]]
        self.max_rank = max(rank_1, rank_2)
        self.min_rank = min(rank_1, rank_2)
        self.max_code = Hand.rank_to_codes_map[self.max_rank]
        self.min_code = Hand.rank_to_codes_map[self.min_rank]

    def is_pair(self):
        return self.max_rank == self.min_rank

    @property
    def value(self):
        return self.max_code + self.min_code
