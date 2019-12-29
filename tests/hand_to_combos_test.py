import pytest

from hand import Hand


@pytest.mark.parametrize("hand_string, dead_cards, expected", [
    ('AK', [], [('As', 'Ks'), ('As', 'Kh'), ('As', 'Kd'), ('As', 'Kc'),
                ('Ah', 'Ks'), ('Ah', 'Kh'), ('Ah', 'Kd'), ('Ah', 'Kc'),
                ('Ad', 'Ks'), ('Ad', 'Kh'), ('Ad', 'Kd'), ('Ad', 'Kc'),
                ('Ac', 'Ks'), ('Ac', 'Kh'), ('Ac', 'Kd'), ('Ac', 'Kc'), ]),
    ('AKs', [], [('As', 'Ks'), ('Ah', 'Kh'), ('Ad', 'Kd'), ('Ac', 'Kc'), ]),
    ('AA', [], [('As', 'Ah'), ('As', 'Ad'), ('As', 'Ac'),
                ('Ah', 'Ad'), ('Ah', 'Ac'),
                ('Ad', 'Ac'), ]),
    ('AK', ['As'], [('Ah', 'Ks'), ('Ah', 'Kh'), ('Ah', 'Kd'), ('Ah', 'Kc'),
                    ('Ad', 'Ks'), ('Ad', 'Kh'), ('Ad', 'Kd'), ('Ad', 'Kc'),
                    ('Ac', 'Ks'), ('Ac', 'Kh'), ('Ac', 'Kd'), ('Ac', 'Kc'), ]),
    ('AK', ['As', 'Ah'], [('Ad', 'Ks'), ('Ad', 'Kh'), ('Ad', 'Kd'), ('Ad', 'Kc'),
                          ('Ac', 'Ks'), ('Ac', 'Kh'), ('Ac', 'Kd'), ('Ac', 'Kc'), ]),
    ('AKs', ['3c'], [('As', 'Ks'), ('Ah', 'Kh'), ('Ad', 'Kd'), ('Ac', 'Kc'), ]),

])
def test_get_variants(hand_string, dead_cards, expected):
    combos = Hand(hand_string).get_combos(dead_cards=dead_cards)
    assert set(combos) == set(expected)
