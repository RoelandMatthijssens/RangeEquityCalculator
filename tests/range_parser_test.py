import pytest

from ..range_parser import parse_range


@pytest.mark.parametrize("hand_range,expected", [
    ('QQ+', ['AA', 'KK', 'QQ']),
    ('QQ+, 77+', ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77']),
    ('44+', ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44'])
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
    ('AA-TT, 22-55, 88', ['AA', 'KK', 'QQ', 'JJ', 'TT', '88', '55', '44', '33', '22']),
])
def test_dash_notation(hand_range, expected):
    assert parse_range(hand_range) == expected
