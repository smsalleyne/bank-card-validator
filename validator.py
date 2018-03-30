import random
import sys


card_type = {

    'chase' : '42076702',
    'amex' : '37',
    'mastercard' : '55',
    'discover' : '60',
    'visa' : '44'
}


def user_input(message):
    if sys.version.startswith('2'):
        return raw_input(message)
    else:
        return input(message)


def format_string(string, lower=True):
    if lower:
        return string.lower().strip()
    else:
        return string.title().strip()


def card_number_validator(string):

    """ Implementation of the Luhn Algorithm to determine if number
        sequence is valid for use as a debit/credit card number """

    double = [int(i)*2 for i in string[-2::-2]]
    same = sum([int(i) for i in string[-1::-2]])
    str_double = ''.join(list(map(str, double)))
    total = 0
    for number in str_double:
        total += int(number)
    if (total + same) % 10 == 0:
        return True
    else:
        return False


def number_generator(n):

    """ Randomly generate a string of numbers whose length is determined by 'n' """

    numbers = [random.randrange(0, 10) for i in range(n)]
    return ''.join([str(i) for i in numbers])


def valid_card(string):
    bank = format_string(string)
    running = True
    while running:
        card_number = card_type.get(bank) + number_generator(16 - len(card_type.get(bank)))
        if card_number_validator(card_number) == True:
            running = False
    return card_number
