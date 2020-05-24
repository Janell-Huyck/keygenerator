from random import randint


def makekey():
    new_key = []
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

    # define the seed array of 5 characters
    """
    6 sets of 5
    first item: can not be from same row as any other first item.
    second item: from one row down, one index less (wrap backwards in same row)
    third item: skip three rows up (wrap to bottom), on 4th row,
     same column as first item.
    fourth item: must come from 5th column, cannot be same row as first_row.
    fifth item: random item in skip three rows from third item
    """
    all_first_rows = []
    for i in range(6):
        small_group = []
        # get first seed
        first_row = randint(0, 10)
        while first_row in all_first_rows:
            first_row = randint(0, 10)
        first_column = randint(0, 5)
        small_group.append(character_possibilities[first_row][first_column])
        all_first_rows.append(first_row)

        # get second item
        second_row = first_row + 1
        if second_row > 10:
            second_row -= 10
        second_column = first_column - 1
        small_group.append(character_possibilities[second_row][second_column])

        # get third item
        third_row = second_row - 4
        third_column = first_column
        small_group.append(character_possibilities[third_row][third_column])

        # get fourth item
        fourth_row = randint(0, 10)
        while fourth_row == first_row:
            fourth_row = randint(0, 10)
        fourth_column = 5
        small_group.append(character_possibilities[fourth_row][fourth_column])

        # get fifth item
        fifth_row = third_row + 4
        if fifth_row > 10:
            fifth_row -= 10
        fifth_column = randint(0, 5)
        small_group.append(character_possibilities[fifth_row][fifth_column])

        new_key += small_group
    new_key = "".join(new_key)

    return new_key
