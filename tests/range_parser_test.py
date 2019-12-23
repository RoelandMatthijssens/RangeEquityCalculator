import pytest

from range_parser import parse_range


@pytest.mark.parametrize("hand_range,expected", [
    ('QQ+', ['AA', 'KK', 'QQ']),
    ('QQ+, 77+', ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77']),
    ('44+', ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44']),
    ('AT+', ['AKs', 'AKo', 'AQs', 'AQo', 'AJs', 'AJo', 'ATs', 'ATo']),
    ('KT+', ['KQs', 'KQo', 'KJs', 'KJo', 'KTs', 'KTo']),
    ('AT+, KT+', ['AKs', 'AKo', 'AQs', 'AQo', 'AJs', 'AJo', 'ATs', 'ATo', 'KQs', 'KQo', 'KJs', 'KJo', 'KTs', 'KTo']),
    ('AK-JT', ['AKs', 'AKo', 'KQs', 'KQo', 'QJs', 'QJo', 'JTs', 'JTo']),
    ('76-32', ['76s', '76o', '65s', '65o', '54s', '54o', '43s', '43o', '32s', '32o']),
    ('AQ-97', ['AQs', 'AQo', 'KJs', 'KJo', 'QTs', 'QTo', 'J9s', 'J9o', 'T8s', 'T8o', '97s', '97o']),
    ('A2s+', ['AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s']),
    ('A2s+, QTs+, AJo+', ['AKs', 'AKo', 'AQs', 'AQo', 'AJs', 'AJo', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s',
                          'A3s', 'A2s', 'QJs', 'QTs']),
])
def test_plus_notation(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('QQ', ['QQ']),
    ('KK', ['KK']),
    ('AK, KQ', ['AKs', 'AKo', 'KQs', 'KQo']),
    ('AKo, AQs, AJ', ['AKo', 'AQs', 'AJs', 'AJo']),
])
def test_single_combos(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('QQ-TT', ['QQ', 'JJ', 'TT']),
    ('TT-QQ', ['QQ', 'JJ', 'TT']),
    ('AA-TT, 22-55', ['AA', 'KK', 'QQ', 'JJ', 'TT', '55', '44', '33', '22']),
    ('AK-AT, KQ-KJ', ['AKs', 'AKo', 'AQs', 'AQo', 'AJs', 'AJo', 'ATs', 'ATo', 'KQs', 'KQo', 'KJs', 'KJo']),
    ('AKo-ATo, KQo-KJ', ['AKo', 'AQo', 'AJo', 'ATo', 'KQo', 'KJo']),
    ('AKs-AT, JTs-J8s, 54s-53', ['AKs', 'AQs', 'AJs', 'ATs', 'JTs', 'J9s', 'J8s', '54s', '53s']),
    ('AK-JT, 97s-53s', ['AKs', 'AKo', 'KQs', 'KQo', 'QJs', 'QJo', 'JTs', 'JTo', '97s', '86s', '75s', '64s', '53s']),
])
def test_dash_notation(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('AA, KK, A2, K5', ['AA', 'A2s', 'A2o', 'KK', 'K5s', 'K5o']),
    ('5K', ['K5s', 'K5o']),
])
def test_ordering(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('22-55, QQ+, A9+, 95', ['AA', 'AKs', 'AKo', 'AQs', 'AQo', 'AJs', 'AJo', 'ATs', 'ATo', 'A9s', 'A9o', 'KK', 'QQ',
                             '95s', '95o', '55', '44', '33', '22']),
])
def test_range_combinations(hand_range, expected):
    assert parse_range(hand_range) == expected
