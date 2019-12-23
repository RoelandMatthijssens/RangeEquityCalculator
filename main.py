from arg_parser import parse_args
from range_parser import parse_range

if __name__ == '__main__':
    input_range = parse_args()
    hands = parse_range(input_range)
    print(hands)
