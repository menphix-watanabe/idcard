import datetime
import sys
import argparse
from id_card_permute import checksum

def checksum(num_list):
    # curr_sum = 0
    # weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    # for idx, num_str in enumerate(num_list[:-1]):
    #     curr_sum += int(num_str) * weight[idx]
    # remainder = curr_sum % 11
    # if remainder != 10:
    #     remainder = str(remainder)
    # else:
    #     remainder = 'X'

    remainder = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][sum([int(num_list[i]) * [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2][i] for i in range(17)]) % 11]

    return num_list[-1].upper() == remainder


def main(args):
    input_str = args.input_str
    num_list = [x for x in input_str]

    if len(num_list) != 18:
        print('Invalid: length != 18')
        return 0

    if checksum(num_list):
        print('Valid')
    else:
        print('Invalid')

    return 0

def parse_args():
    parser = argparse.ArgumentParser(description='Checks the validity of an id card number')
    parser.add_argument('input_str', help='Partial ID card string')
    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main(parse_args()))
