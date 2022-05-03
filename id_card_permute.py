import datetime
import sys
import argparse

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


def guess_id_card_missing_birthday(partial_num: str):
    '''
    Given a partially redacted ID card number, return all the possible
    permutations. Redaction is marked as '?'. E.g. 110107????????2456
    :param partial_num:
    :return:
    '''
    if len(partial_num) != 18:
        print('Length must be 18!', file=sys.stderr)
        return False

    now = datetime.datetime.now()
    # 1 1 0 1 0 7 ? ? ? ?  ?  ?  ?  ?  2  4  5  6
    # 0 1 2 3 4 5 6 7 8 9  10 11 12 13 14 15 16 17
    num_list = [x for x in partial_num]
    for idx, num_str in enumerate(num_list):
        if (idx < 6 or idx > 13) and num_str == '?':
            print('Cannot have unknown other than birthday', file=sys.stderr)
            return False

    for year in range(1900, now.year + 1):
        is_leapyear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        for month in range(1, 13):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                max_days = 31
            elif month != 2:
                max_days = 30
            else:
                if is_leapyear:
                    max_days = 29
                else:
                    max_days = 28
            for day in range(1, max_days + 1):
                new_list = num_list.copy()
                year_str = '{0}'.format(year)
                for i in range(4):
                    new_list[6 + i] = year_str[i]
                month_str = '{0:02d}'.format(month)
                new_list[10] = month_str[0]
                new_list[11] = month_str[1]
                day_str = '{0:02d}'.format(day)
                new_list[12] = day_str[0]
                new_list[13] = day_str[1]
                # print('Checking ' + ''.join(new_list))
                if checksum(new_list):
                    print(''.join(new_list))
    return True


def main(args):
    input_str = args.input_str
    if not guess_id_card_missing_birthday(input_str):
        return 1

    return 0

def parse_args():
    parser = argparse.ArgumentParser(description='Guess all the possible combinations of ID card number')
    parser.add_argument('input_str', help='Partial ID card string')
    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main(parse_args()))