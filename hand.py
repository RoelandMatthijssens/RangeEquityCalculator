from enum import Enum


class Suitedness(Enum):
    UNDEFINED = ''
    SUITED = 's'
    OFFSUIT = 'o'

    @staticmethod
    def compare(a, b):
        if a == Suitedness.SUITED and b == Suitedness.OFFSUIT:
            return -1
        elif a == Suitedness.OFFSUIT and b == Suitedness.SUITED:
            return 1
        else:
            return 0


class Hand:
    codes_to_rank_map = {
        '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
        'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12
    }
    rank_to_codes_map = {
        0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9',
        8: 'T', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'
    }

    def __init__(self, hand_string=None):
        [max_rank, min_rank, max_code, min_code, suitedness] = self.__parse_hand_string(hand_string)
        self.max_rank = max_rank
        self.min_rank = min_rank
        self.max_code = max_code
        self.min_code = min_code
        self.suitedness = suitedness

    def __eq__(self, other):
        return Hand.compare(self, other) == 0

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_ranks(cls, a, b, s=Suitedness.UNDEFINED):
        return cls(cls.rank_to_codes_map[a] + cls.rank_to_codes_map[b] + s.value)

    @classmethod
    def from_codes(cls, a, b, s=Suitedness.UNDEFINED):
        return cls(a + b + s.value)

    @property
    def is_pair(self):
        return self.max_rank == self.min_rank

    @property
    def is_suited(self):
        return self.suitedness == Suitedness.SUITED

    @property
    def is_offsuit(self):
        return self.suitedness == Suitedness.OFFSUIT

    @property
    def value(self):
        return self.max_code + self.min_code + self.suitedness.value

    @property
    def variants(self):
        if self.is_pair or self.is_offsuit or self.is_suited:
            return [self]
        else:
            suited = Hand.from_codes(self.max_code, self.min_code, Suitedness.SUITED)
            offsuit = Hand.from_codes(self.max_code, self.min_code, Suitedness.OFFSUIT)
            return [suited, offsuit]

    @staticmethod
    def compare(a, b):
        if a.max_rank > b.max_rank:
            return -1
        if b.max_rank > a.max_rank:
            return 1
        if a.min_rank > b.min_rank:
            return -1
        if b.min_rank > a.min_rank:
            return 1
        else:
            return Suitedness.compare(a.suitedness, b.suitedness)

    @staticmethod
    def __parse_hand_string(hand_string):
        rank_1 = Hand.codes_to_rank_map[hand_string[0]]
        rank_2 = Hand.codes_to_rank_map[hand_string[1]]
        max_rank = max(rank_1, rank_2)
        min_rank = min(rank_1, rank_2)
        if len(hand_string) > 2:
            suite = Suitedness.SUITED if hand_string[2] == 's' else Suitedness.OFFSUIT
        else:
            suite = Suitedness.UNDEFINED
        return [
            max_rank,
            min_rank,
            Hand.rank_to_codes_map[max_rank],
            Hand.rank_to_codes_map[min_rank],
            suite
        ]

    def get_combos(self):
        SUITES = ['s', 'h', 'd', 'c', ]
        combos = [(self.max_code + i, self.min_code + j) for i in SUITES for j in SUITES]
        return combos
