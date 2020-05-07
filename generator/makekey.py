import random

""" ascii chtrs from 48 - 122(inclusive), excluding 58-64(inclusive)
"""


def makekey():
    character_possibilities = ['a', 'b', 'c', 'd', 'e', 'f',
                               'g', 'h', 'i', 'j', 'k', 'l',
                               'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x',
                               'y', 'z', 'A', 'B', 'C', 'D',
                               'E', 'F', 'G', 'H', 'I', 'J',
                               'K', 'L', 'M', 'N', 'O', 'P',
                               'Q', 'R', 'S', 'T', 'U', 'V',
                               'W', 'X', 'Y', 'Z', '0', '1',
                               '2', '3', '4', '5', '6', '7',
                               '8', '9']
    random_number = random.randint(0, len(character_possibilities))
    return random_number
