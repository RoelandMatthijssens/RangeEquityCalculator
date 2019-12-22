class Range():
    codes_to_rank_map = {
        '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
        'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12
    }
    rank_to_codes_map = {
        0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9',
        8: 'T', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'
    }

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
        a = self.range_string.strip('+')
        rank_11 = Range.codes_to_rank_map[a[0]]
        rank_12 = Range.codes_to_rank_map[a[1]]
        if rank_11 == rank_12:
            return self.min_to_max('AA', a)
        else:
            highest_card = max(rank_11, rank_12)
            lowest_card = min(rank_11, rank_12)
            top_hand = Range.rank_to_codes_map[highest_card] + Range.rank_to_codes_map[highest_card - 1]
            bottom_hand = Range.rank_to_codes_map[highest_card] + Range.rank_to_codes_map[lowest_card]
            return self.min_to_max(bottom_hand, top_hand)

    def dash_range(self):
        top, bottom = self.range_string.split('-')
        return self.min_to_max(top, bottom)

    def single_hand(self):
        rank_11 = Range.codes_to_rank_map[self.range_string[0]]
        rank_12 = Range.codes_to_rank_map[self.range_string[1]]
        low_card = min(rank_11, rank_12)
        high_card = max(rank_11, rank_12)
        return Range.rank_to_codes_map[high_card] + Range.rank_to_codes_map[low_card]

    def min_to_max(self, a, b):
        if a[0] == a[1] and b[0] == b[1]:
            return self.min_to_max_pairs(a, b)
        elif a[0] == b[0] and a[1] != b[1]:
            return self.min_to_max_non_pairs(a, b)
        else:
            return self.min_to_max_connectors_and_gappers(a, b)

    @staticmethod
    def min_to_max_connectors_and_gappers(a, b):
        rank_11 = Range.codes_to_rank_map[a[0]]
        rank_21 = Range.codes_to_rank_map[b[0]]
        rank_22 = Range.codes_to_rank_map[b[1]]
        result = []
        while rank_11 >= rank_21:
            hand = Range.rank_to_codes_map[rank_21] + Range.rank_to_codes_map[rank_22]
            result.append(hand)
            rank_21 += 1
            rank_22 += 1
        return result

    @staticmethod
    def min_to_max_pairs(a, b):
        rank_a = Range.codes_to_rank_map[a[0]]
        rank_b = Range.codes_to_rank_map[b[0]]
        top = max(rank_a, rank_b)
        bottom = min(rank_a, rank_b)
        return [Range.rank_to_codes_map[i] * 2 for i in range(bottom, top + 1)]

    @staticmethod
    def min_to_max_non_pairs(a, b):
        rank_12 = Range.codes_to_rank_map[a[1]]
        rank_22 = Range.codes_to_rank_map[b[1]]
        min_rank_2 = min(rank_12, rank_22)
        max_rank_2 = max(rank_12, rank_22)
        return [a[0] + Range.rank_to_codes_map[i] for i in range(min_rank_2, max_rank_2 + 1)]