import pytest

from hand import Hand


@pytest.mark.parametrize("hand_string,expected", [
    ('AK', [('As', 'Ks'), ('As', 'Kh'), ('As', 'Kd'), ('As', 'Kc'),
            ('Ah', 'Ks'), ('Ah', 'Kh'), ('Ah', 'Kd'), ('Ah', 'Kc'),
            ('Ad', 'Ks'), ('Ad', 'Kh'), ('Ad', 'Kd'), ('Ad', 'Kc'),
            ('Ac', 'Ks'), ('Ac', 'Kh'), ('Ac', 'Kd'), ('Ac', 'Kc'), ]),
    ('AKs', [('As', 'Ks'), ('Ah', 'Kh'), ('Ad', 'Kd'), ('Ac', 'Kc'), ]),
    ('AA', [('As', 'Ah'), ('As', 'Ad'), ('As', 'Ac'),
            ('Ah', 'Ad'), ('Ah', 'Ac'),
            ('Ad', 'Ac'), ]),
])
def test_get_variants(hand_string, expected):
    combos = Hand(hand_string).get_combos()
    assert set(combos) == set(expected)
