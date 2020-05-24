"""
6 sets of 5
first item: can not be from same row as any other first item.
second item: from one row down, one index less (wrap backwards in same row)
third item: skip three rows up (wrap to bottom)
 and then on 4th row, same column as first item.
fourth item: must come from 5th column, cannot be same row as first_row.
fifth item: random item in skip three rows from third item
"""


def decodekey(test_key):

    character_possibilities = [
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['g', 'h', 'i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p', 'q', 'r'],
        ['s', 't', 'u', 'v', 'w', 'x'],
        ['y', 'z', 'A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z', '0', '1'],
        ['2', '3', '4', '5', '6', '7'],
        ['8', '9', ':', '!', '@', '$']]

    # break into groups of five
    if len(test_key) == 30:
        test_key_list = []
        for letter in test_key:
            test_key_list.append(letter)
        all_firsts = []
        for i in range(6):
            first_row = None
            # select first item
            first_item = test_key_list.pop(0)
            # determine what row first_item is in
            for row in range(11):
                if first_item in character_possibilities[row]:
                    first_row = row
            if first_row is None:
                return False
            if first_row in all_firsts:
                return False

            # add it to the collection of first items
            all_firsts.append(first_row)

            # determine first column
            first_column = character_possibilities[first_row].index(first_item)

            # select second item
            second_item = test_key_list.pop(0)
            # must be one row down
            test_second_row = first_row + 1
            if test_second_row > 10:
                test_second_row -= 10
            if second_item not in character_possibilities[test_second_row]:
                return False
            else:
                second_row = test_second_row
            # must be one index less
            test_second_column = first_column - 1
            if second_item != character_possibilities[
                    second_row][test_second_column]:
                return False

            # select third item
            # must be 4 rows down, same column as item 1
            third_item = test_key_list.pop(0)
            test_third_row = second_row - 4
            if third_item == character_possibilities[
                    test_third_row][first_column]:
                third_row = test_third_row
            else:
                return False

            # fourth item is column 5, not row of first_item
            fourth_item = test_key_list.pop(0)
            fourth_row = None
            for row in range(11):
                if fourth_item == character_possibilities[row][5]:
                    fourth_row = row
            if fourth_row is None:
                return False
            if fourth_row == first_row:
                return False

            # fifth item is random item 4 rows below third_row
            fifth_item = test_key_list.pop(0)
            test_fifth_row = third_row + 4
            if test_fifth_row > 10:
                test_fifth_row -= 10
            if fifth_item not in character_possibilities[test_fifth_row]:
                return False
        return True
    return False
