import pytest

from ..hand import Hand


@pytest.mark.parametrize("hand_string,expected", [
    ('QQ', ['QQ']),
    ('AK', ['AKs', 'AKo']),
    ('AKs', ['AKs']),
    ('AKo', ['AKo']),
])
def test_get_variants(hand_string, expected):
    variants = [i.value for i in Hand(hand_string).variants]
    assert variants == expected
