from functools import reduce

from holdem_calc import calculate

from range_parser import range_to_hands


def hand_vs_hand(hand1, hand2, board):
    tie, win1, win2 = calculate(board, False, 1000, None, [hand1[0], hand1[1], hand2[0], hand2[1]], False)
    return {
        'Tie': tie,
        'Player1': win1,
        'Player2': win2
    }


def hand_vs_range(hand, hand_range, board=None):
    if board is None:
        board = []
    dead_cards = board + list(hand)
    combos = reduce(list.__add__, [hand.get_combos(dead_cards) for hand in range_to_hands(hand_range)])
    results = {
        'Tie': [],
        'Player1': [],
        'Player2': [],
    }

    for combo in combos:
        win_percentages = hand_vs_hand(hand, combo, board)
        results['Tie'].append(win_percentages['Tie'])
        results['Player1'].append(win_percentages['Player1'])
        results['Player2'].append(win_percentages['Player2'])

    print_results(hand, hand_range, results, board)


def valid_hands(hand1, hand2):
    for card in hand1:
        if card in hand2:
            return False
    return True


def range_vs_range(range1, range2, board=None):
    if board is None:
        board = []
    results = {
        'Tie': [],
        'Player1': [],
        'Player2': [],
    }
    player1_combos = reduce(list.__add__, [hand.get_combos() for hand in range_to_hands(range1)])
    player2_combos = reduce(list.__add__, [hand.get_combos() for hand in range_to_hands(range2)])
    for player1_combo in player1_combos:
        for player2_combo in player2_combos:
            if not valid_hands(player1_combo, player2_combo):
                continue
            win_percentages = hand_vs_hand(player1_combo, player2_combo, board)
            results['Tie'].append(win_percentages['Tie'])
            results['Player1'].append(win_percentages['Player1'])
            results['Player2'].append(win_percentages['Player2'])
    print_results(range1, range2, results, board)


def print_results(player1_input, player2_input, results, board):
    total_tie = sum(results['Tie']) / len(results['Tie'])
    total_player_1 = sum(results['Player1']) / len(results['Tie'])
    total_player_2 = sum(results['Player2']) / len(results['Tie'])
    print('Board', board)
    print(''.join(player1_input), total_player_1)
    print(''.join(player2_input), total_player_2)
    print('Tie', total_tie)


if __name__ == '__main__':
    hand_vs_range(('As', 'Ah'), '99+', ["8s", "7s", "6c"])
