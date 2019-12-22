import pytest

from ..range_parser import parse_range


@pytest.mark.parametrize("hand_range,expected", [
    ('QQ+', ['AA', 'KK', 'QQ']),
    ('QQ+, 77+', ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77']),
    ('44+', ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44']),
    ('AT+', ['AK', 'AQ', 'AJ', 'AT']),
    ('KT+', ['KQ', 'KJ', 'KT']),
    ('AT+, KT+', ['AK', 'AQ', 'AJ', 'AT', 'KQ', 'KJ', 'KT']),
])
def test_plus_notation(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('QQ', ['QQ']),
    ('KK', ['KK']),
    ('AK, KQ', ['AK', 'KQ']),
])
def test_single_combos(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('QQ-TT', ['QQ', 'JJ', 'TT']),
    ('TT-QQ', ['QQ', 'JJ', 'TT']),
    ('AA-TT, 22-55', ['AA', 'KK', 'QQ', 'JJ', 'TT', '55', '44', '33', '22']),
    ('AK-AT, KQ-KJ', ['AK', 'AQ', 'AJ', 'AT', 'KQ', 'KJ']),
])
def test_dash_notation(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('AA, KK, A2, K5', ['AA', 'A2', 'KK', 'K5']),
    ('5K', ['K5']),
])
def test_ordering(hand_range, expected):
    assert parse_range(hand_range) == expected


@pytest.mark.parametrize("hand_range,expected", [
    ('22-55, QQ+, A9+, 95', ['AA', 'AK', 'AQ', 'AJ', 'AT', 'A9', 'KK', 'QQ', '95', '55', '44', '33', '22']),
])
def test_range_combinations(hand_range, expected):
    assert parse_range(hand_range) == expected
